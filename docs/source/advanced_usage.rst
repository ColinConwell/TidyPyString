Advanced Usage
=============

This section provides examples of more advanced usage patterns and combinations of tidystring functions.

Data Cleaning Workflow
--------------------

Combining multiple functions for effective data cleaning:

.. code-block:: python

    import pandas as pd
    from tidystring import str_trim, str_remove, str_to_lower, str_replace

    # Example messy data
    messy_data = pd.Series([
        "  Product A - $19.99  ",
        " PRODUCT B - $25.50 ",
        "product c - $15.75"
    ])

    # Clean data in one pipeline
    clean_data = (
        messy_data
        .pipe(str_trim)                         # Remove whitespace
        .pipe(str_to_lower)                     # Standardize case
        .pipe(str_replace, " - ", ": ")         # Standardize separator
        .pipe(str_replace, "$", "USD ")         # Standardize currency
    )

    print(clean_data)
    # 0    product a: USD 19.99
    # 1    product b: USD 25.50
    # 2    product c: USD 15.75
    # dtype: object

Text Processing with Regular Expressions
--------------------------------------

Using regular expressions for more complex text processing:

.. code-block:: python

    import pandas as pd
    from tidystring import str_extract, str_replace, str_search_recase

    # Extract structured information from text
    texts = [
        "Name: John Smith, Age: 35, Email: john@example.com",
        "Name: Jane Doe, Age: 28, Email: jane@example.com",
        "Name: Bob Johnson, Age: 42, Email: bob@example.com"
    ]

    # Extract names
    names = str_extract(texts, "Name: ([^,]+)")
    print(names)
    # ['John Smith', 'Jane Doe', 'Bob Johnson']

    # Extract emails and convert to uppercase
    emails = str_extract(texts, "Email: ([^,]+)")
    uppercase_emails = str_to_upper(emails)
    print(uppercase_emails)
    # ['JOHN@EXAMPLE.COM', 'JANE@EXAMPLE.COM', 'BOB@EXAMPLE.COM']

    # Format text with multiple operations
    formatted = str_search_recase(texts, "Name: ([^,]+)", "upper")
    formatted = str_replace(formatted, "Age: ", "AGE: ")
    print(formatted)
    # ['NAME: JOHN SMITH, AGE: 35, Email: john@example.com',
    #  'NAME: JANE DOE, AGE: 28, Email: jane@example.com',
    #  'NAME: BOB JOHNSON, AGE: 42, Email: bob@example.com']

Working with DataFrames
---------------------

Integrating tidystring with pandas DataFrames:

.. code-block:: python

    import pandas as pd
    from tidystring import str_detect, str_extract, str_remove, str_to_title

    # Sample dataset
    df = pd.DataFrame({
        'product': ['Laptop Pro 13"', 'Tablet Air 10"', 'Phone Mini 5"'],
        'sku': ['LP-13-2022', 'TA-10-2022', 'PM-5-2022'],
        'price': ['$1299.99', '$599.99', '$799.99']
    })

    # Extract size information
    df['size'] = str_extract(df['product'], '(\\d+)"')

    # Remove price symbol
    df['price_clean'] = str_remove(df['price'], '\\$')

    # Create product category column
    df['category'] = str_extract(df['product'], '^(\\w+)')
    df['category'] = str_to_title(df['category'])

    # Filter rows containing "Pro" in product name
    pro_products = df[str_detect(df['product'], 'Pro')]

    print(df)
    # Output:
    #           product        sku     price size price_clean category
    # 0    Laptop Pro 13"  LP-13-2022  $1299.99   13     1299.99   Laptop
    # 1    Tablet Air 10"  TA-10-2022   $599.99   10      599.99   Tablet
    # 2     Phone Mini 5"   PM-5-2022   $799.99    5      799.99    Phone

Custom Use Cases
--------------

Some examples of custom use cases combining multiple functions:

.. code-block:: python

    import pandas as pd
    from tidystring import (
        str_extract, str_split, str_replace, str_trim,
        str_to_lower, str_to_upper, str_concat
    )

    # Normalizing names
    names = ["  John SMITH  ", "Jane DOE", "BOB johnson"]
    
    # Extract first and last names, normalize case
    first_names = [str_trim(name).split()[0] for name in names]
    last_names = [str_trim(name).split()[1] for name in names]
    
    normalized = str_concat(
        str_to_title(first_names),
        str_to_upper(last_names),
        sep=" "
    )
    
    print(normalized)
    # ['John SMITH', 'Jane DOE', 'Bob JOHNSON']

    # Parsing URLs
    urls = [
        "https://example.com/products?id=123",
        "http://example.org/about",
        "https://api.example.net/v2/users/456"
    ]
    
    # Extract domains
    domains = str_extract(urls, "://([^/]+)")
    print(domains)
    # ['example.com', 'example.org', 'api.example.net']
    
    # Extract path
    paths = str_extract(urls, "://[^/]+(/[^?]*)")
    print(paths)
    # ['/products', '/about', '/v2/users/456']

    # Format as markdown links
    markdown_links = [
        f"[{str_to_upper(domain)}]({url})" 
        for domain, url in zip(domains, urls)
    ]
    print(markdown_links)
    # ['[EXAMPLE.COM](https://example.com/products?id=123)',
    #  '[EXAMPLE.ORG](http://example.org/about)',
    #  '[API.EXAMPLE.NET](https://api.example.net/v2/users/456)']