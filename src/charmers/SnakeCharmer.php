<?php

namespace ThunderbirdDeveloper\Bifrost;

class SnakeCharmer {

    private $files = array();
    private $results = array();
    private $command;
    private $format;
    private $path = __DIR__."/snakes/";

    /**
     * Constructor of the SnakeCharmer class.
     *
     * @param mixed $files List of paths to Python script files.
     * @param string $format Format of the command invoking the Python script.
     * @return void
     */
    function __construct($files = null, $format = 'python %s %s')
    {
        if (isset($files)) {
            $this->setScripts($files);
        }
        $this->format = $format;
    }

    /**
     * Checks and corrects the format of the Python script filename.
     *
     * @param string $file Path to the Python script file.
     * @return void
     */
    function checkPythonFormat(&$file)
    {
        $pos = strpos($file,".py");
        if ($pos === false) {
            $file .='.py';
        }
    }

    /**
     * Set path.
     *
     * @param string $path Path to the Python script file directory.
     * @return void
     */
    function setPath($path) {
        $this->path = $path;
    }

    /**
     * Clears the list of script files.
     *
     * @return void
     */
    function clearListScripts() {
        $this->files = array();
    }

    /**
     * Clears the results of script execution.
     *
     * @return void
     */
    function clearResult() {
        $this->results = array();
    }

    /**
     * Sets the list of script files.
     *
     * @param mixed $files List of paths to Python script files.
     * @param bool $clearResult Determines whether to clear the results beforehand.
     * @return void
     */
    function setScripts($files, $clearResult = true) {
        if ($clearResult) {
            $this->clearResult();
        }
        $this->clearListScripts();
        $this->appendScripts($files);
    }

    /**
     * Appends script files to the list.
     *
     * @param mixed $files List of paths to Python script files.
     * @return void
     */
    function appendScripts($files) {
        if (is_string($files)) {
            $this->checkPythonFormat($files);
            array_push($this->files, $this->path.$files);
        } else {
            foreach ($files as $file) {
                $this->checkPythonFormat($file);
                array_push($this->files, $this->path.$file);
            }
        }
    }

    /**
     * Executes the scripts.
     *
     * @param mixed $files List of paths to Python script files.
     * @param string $params Parameters passed to the scripts.
     * @return void
     */
    function execute($files, $params = '')
    {
        $this->appendScripts($files);
        $this->run($params, true);
        array_pop($this->files);
    }

    /**
     * Executes multiple scripts with different parameters.
     *
     * @param array $params Array of parameters for each script.
     * @return void
     */
    function runManyParams($params)
    {
        foreach ($params as $param) {
            $this->run($param);
        }
    }

    /**
     * Executes the scripts.
     *
     * @param string $params Parameters passed to the scripts.
     * @param bool $last Specifies whether to execute only the last script on the list.
     * @return void
     */
    function run($params = '', $last = false)
    {
        $list = $this->files;
        if ($last) {
            $list = array(end($list));
        }
        foreach ($list as $file) {
            $this->command = escapeshellcmd(sprintf($this->format, $file, $params));
            $output = shell_exec($this->command);
            if (empty($output)) {
                $output = exec($this->command.'2>logs/shell_exec_error.log');
            }
            array_push($this->results, rtrim($output));
        }
    }

    /**
     * Displays the results on standard output.
     *
     * @return void
     */
    function showResult()
    {
        if (!empty($this->results)) {
            foreach ($this->results as $result) {
                echo $result;
            }
        }
    }

    /**
     * Returns the results as a single string.
     *
     * @param string $separator Separator between results.
     * @return string Results as a single string.
     */
    function getResultAsString($separator = "\n")
    {
        return rtrim(implode($separator, $this->results));
    }

    /**
     * Returns the results as an array.
     *
     * @return array Results as an array.
     */
    function getResultAsArray()
    {
        return $this->results;
    }
}
?>