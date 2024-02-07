<?php

require 'src/charmers/SnakeCharmer.php';
require 'vendor/autoload.php'; 

use PHPUnit\Framework\TestCase;
use ThunderbirdDeveloper\Bifrost\SnakeCharmer;

/*
 *  composer install
 *  vendor/bin/phpunit test/SnakeCharmerTest.php 
 */

class SnakeCharmerTest extends TestCase
{
    private $snakeCharmer;

    const SCRIPT = [
        'helloworld' => 'example/helloworld.py',
        'message' => 'example/message.py',
        'primenumbers' => 'example/primenumbers.py',
        'fibonaci' => 'example/fibonaci.py',
        'pell' => 'example/pell.py',
      ];

    protected function setUp(): void
    {
        parent::setUp();
        $this->snakeCharmer = new SnakeCharmer();
    }

    public function testHelloworldScriptExecution(): void
    {
        $this->snakeCharmer->execute(self::SCRIPT['helloworld']);
        $result = $this->snakeCharmer->getResultAsString();
        $this->assertEquals("Hello, world!", $result);
    }

    public function testMessageScriptExecution(): void
    {
        $this->snakeCharmer->execute('example/message.py', '--text "Test 1"');
        $result = $this->snakeCharmer->getResultAsString();
        $this->assertNotEquals("Test 2", $result);
    }

    public function testPrimenumbersScriptExecution(): void
    {
        $this->snakeCharmer->setScripts(self::SCRIPT['primenumbers']);
        $this->snakeCharmer->run('--range 20 --or');
        $result = $this->snakeCharmer->getResultAsString();
        $this->assertEquals("[2, 3, 5, 7, 11, 13, 17, 19]", $result);

        $this->snakeCharmer->clearResult();
        $this->snakeCharmer->run('--get 20 --or');
        $result = $this->snakeCharmer->getResultAsString();
        $this->assertEquals("19", $result);
    }

    public function testFibonaciScriptExecution(): void
    {
        $this->snakeCharmer->setScripts(self::SCRIPT['fibonaci']);
        $this->snakeCharmer->run('--range 12 --or');
        $result = $this->snakeCharmer->getResultAsString();
        $this->assertEquals("[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]", $result);

        $this->snakeCharmer->clearResult();
        $this->snakeCharmer->run('--get 11 --or');
        $result = $this->snakeCharmer->getResultAsString();
        $this->assertEquals("55", $result);
    }

    public function testPellScriptExecution(): void
    {
        $this->snakeCharmer->setScripts(self::SCRIPT['pell']);
        $this->snakeCharmer->run('--range 12 --or');
        $result = $this->snakeCharmer->getResultAsString();
        $this->assertEquals("[0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741]", $result);

        $this->snakeCharmer->clearResult();
        $this->snakeCharmer->run('--get 11 --or');
        $result = $this->snakeCharmer->getResultAsString();
        $this->assertEquals("2378", $result);
    }

    public function testManyParamsExecution(): void
    {
        $this->snakeCharmer->setScripts(self::SCRIPT['primenumbers']);
        $this->snakeCharmer->appendScripts(self::SCRIPT['fibonaci']);
        $this->snakeCharmer->appendScripts(self::SCRIPT['pell']);
        $this->snakeCharmer->runManyParams(['--get 10 --or','--get 9 --or']);
        $result = $this->snakeCharmer->getResultAsString(',');
        $this->assertEquals("7,34,985,7,21,408", $result);
    }
}
