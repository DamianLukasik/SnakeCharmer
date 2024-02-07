# Snake Charmer

Snake Charmer is a simple PHP class designed to execute Python scripts conveniently from within a PHP environment. It provides methods to run Python scripts, pass parameters to them, and retrieve the results.

## Features

- Execute Python scripts from PHP with ease.
- Pass parameters to Python scripts.
- Retrieve results as strings or arrays.
- Clear script files and results conveniently.

## Installation

You can install Snake Charmer via Composer. Run the following command in your terminal:

```bash
composer require thunderbirddeveloper/bifrost/snakecharmer
```

## Usage

Here's a basic example of how to use Snake Charmer:

```php
<?php

require 'vendor/autoload.php'; 

use ThunderbirdDeveloper\Bifrost\SnakeCharmer;

// Instantiate SnakeCharmer
$snakeCharmer = new SnakeCharmer();

// Set the script file
$snakeCharmer->setScripts('example/script.py');

// Run the script
$snakeCharmer->run();

// Get the result as a string
$result = $snakeCharmer->getResultAsString();
echo $result; // Output the result
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Damian Łukasik 08.02.2024