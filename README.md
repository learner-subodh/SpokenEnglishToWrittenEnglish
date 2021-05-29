# Spoken English To Written English


This is a Python module to convert a paragraph of spoken english to written english.

Note that we are not converting audio to text; we are converting just a raw transcript from spoken English to written English. This is a simple protocol based program so the range of inputrs that it can accept isn't that wide. 


## Installation:
  
  You can install the module using the below command.
   ```
   $ python3 setup.py install
   ```
  Instead, if you don't want to actually install it but still would like to use it. Then do,
   ```
   $ python setup.py develop
   ``` 


## Usage:

   ```
    $from ConvertSpokenToWritten import SpokenToWritten 
    $SpokenToWritten.sp_to_wr()

    ** Welcome **

    [ENTER INPUT PARAGRAPH] : Please enter paragraph including spoken English:
            Hey, you know what, the best way to get triple 4 using just an 11 is by multiplying hundred by 4. If you will start at 5 A M, you will be done with this humongous task and it will still be 5 A M. Hope you liked the trick ;)

    Written English paragraph for the given input paragraph:

     " Hey, you know what, the best way to get 444 using just an 11 is by multiplying hundred by 4. If you will start at 5 AM, you will be done with this humongous task and it will still be 5 AM. Hope you liked the trick ;)"
```


## Raising issues for Bugs/Errors

   If you find any bugs/errors in the usage of above code, please raise an issue through  
   [Github](https://github.com/learner-subodh/SpokenEnglishToWrittenEnglish)


## Scope for possible future functionalities that can be added in the future versions of the module:

1. Functionalitiees related to conversion of currencies, amounts or any floating point numericals.
2. Handling of mutiple number systems after choosing one from provided dropdown.
3. Handling grammatical details.
4. Handling dates in multiple formats like dd/mm/yyyy or mm/dd/yyyy.
5. Deployment of above system like a web app using either Flask, HTML, CSS or using Streamlit & GitHub. 


## License


GNU General Public License v3.0

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.
