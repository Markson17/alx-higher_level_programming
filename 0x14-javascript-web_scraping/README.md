# JavaScript Web Scraping Task

This repository contains a set of JavaScript scripts that perform different tasks. Each script is described below along with the instructions on how to run it.

## Reading a file
`0-readFile.js` is a script that reads and prints the content of a file. The script takes the file path as the first argument and reads the file in utf-8 format. If an error occurs during the reading process, the error object will be printed.

To run the script, open a terminal window and type the following command:
```
node 0-readFile.js [file path]
```

## Writing to a file
`1-writeFile.js` is a script that writes a string to a file. The script takes the file path as the first argument and the string to write as the second argument. The content of the file will be written in utf-8 format. If an error occurs during the writing process, the error object will be printed.

To run the script, open a terminal window and type the following command:
```
node 1-writeFile.js [file path] [string to write]
```

## Displaying the status code of a GET request
`2-statusCode.js` is a script that displays the status code of a GET request. The script takes the URL to request as the first argument and uses the `request` module to make the request. The status code will be printed in the format: `code: [status code]`.

To run the script, open a terminal window and type the following command:
```
node 2-statusCode.js [URL]
```

## Counting movies with a character
`4-starwars_count.jss` is a script that prints the number of movies where the character "Wedge Antilles" is present. The script takes the API URL of the Star Wars API as the first argument and filters the result of the API by the character ID of Wedge Antilles. The `request` module is used to make the API request.

To run the script, open a terminal window and type the following command:
```
node 4-starwars_count.js [API URL]
```

## Getting the contents of a webpage and storing it in a file
`5-request_store.js` is a script that gets the contents of a webpage and stores it in a file. The script takes the URL to request as the first argument and the file path to store the response as the second argument. The file will be UTF-8 encoded. The `request` module is used to make the request.

To run the script, open a terminal window and type the following command:
```
node 5-request_store.js [URL] [file path]
```