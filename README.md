    # COMPLIMENTIFY
    #### Video Demo:  <URL HERE>
    #### Description:

**Project Description:**

The program is a simple interactive script that prompts the user with questions and generates a compliment for them. It utilizes various modules and external files to enhance the user experience. The program's main purpose is to provide a fun and uplifting interaction for the user.

**Files and their Functions:**

1) **main.py**: This is the main script that runs the program. It imports the necessary modules and contains the main() function, which is responsible for the overall flow of the **program.
2) **compliment.db**: This file is a SQLite database that stores a collection of compliments. The **get_random_compliment()** function in main.py retrieves a random compliment from this database.
3) **greetings.db**: This file is another SQLite database that stores a collection of greetings. **The get_random_greeting()** function in main.py retrieves a random greeting from this database.
4) **no_response.db**: This file is an SQLite database that stores a collection of responses for when the user does not want to proceed with the program. The **get_random_no_response()** function in main.py retrieves a random response from this database.
5) **cowsay**: This module is used to generate ASCII art of a cow saying the compliment. The cowsay_output variable in main.py stores the generated ASCII art.
6) **PIL**: This module is used to convert the ASCII art into a PNG image. The output_to_png() function in main.py takes the ASCII art as input and saves it as a PNG file.
7) **subprocess**: This module is used to execute the cowsay command and capture its output. The cowsay_output variable in main.py stores the output of the cowsay command.
8) **sys**: This module is used to exit the program when the user chooses not to proceed.

**Design Choices:**

The program utilizes external databases (compliment.db, greetings.db, no_response.db) to store collections of compliments, greetings, and responses. This design choice allows for easy modification and expansion of the available options without modifying the code.

The program also uses the cowsay module to generate ASCII art of a cow saying the compliment. This adds a fun and interactive element to the program.

Additionally, the program provides the option to output the compliment as a PNG image. This feature enhances the visual presentation of the compliment and allows the user to save and share it easily.

The design choices aim to create an engaging and enjoyable user experience.

**Versions:**

**complimentify.py**: This is a basic version of complimentify that user for series of questions and generate an output based on the repsonse given. 

**complimentify_c.py**: This is a basic version of complimentify with comprehensive comments for each line to help viewers understand the flow of code.

**complimentify_png.py**: This is the current version of the program, which generates a compliment and alaso give an extra features to output the compliment in png format in a light mode style. It is similar to main.py but with some modifications to the design.

**complimentify_png_c.py**: This is the program version, which generates a compliment and a PNG output in a light mode style with comprehensive comments for each line to help viewers understand the code flow.

**complimentify_bw_png.py**: This is another program version, which generates a compliment and a png output in a dark mode style. It is similar to main.py but with some modifications to the design.


**Additional:**

**test_complimetify.py**: This is a test script that tests the program's functionality.

