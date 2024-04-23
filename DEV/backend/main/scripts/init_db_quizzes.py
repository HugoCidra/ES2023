import bcrypt
from api.models import *
from api.REQ3.views import new_quiz

# run with python manage.py runscript init_db

def run():
    #quizzes
    new_quiz(
{
    "tags": ["AC"],
    "body": "Consider a MIPS processor. Suppose you want to divide a number by 8. Consider that the corresponding statement in C for that number would be int num;. Which of the following instructions correctly divides the number by 8? Note: remember that the number can be negative.",
    "opt_text": "",
    "options": [
        {
            id: 1,
            "body": "srl $a0,$a0,3",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 2,
            "body": "sra $a0,$a0,3",
            "is_correct": True,
            "justification": "",
        },
        {
            id: 3,
            "body": "sra $a0,$a0,8",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 4,
            "body": "div $a0,$a0,3",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 5,
            "body": "srl $a1,$a0,8",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 6,
            "body": "sra $a0,$a0,8",
            "is_correct": False,
            "justification": "",
        },
    ],
},
User.objects.get(id=1),
4,
)
    new_quiz(
    {
        "tags": ["AC"],
        "body": "The ori instruction has a 16-bit immediate value. How would you decompose the MIPS assembly instruction ori $s4,$s2, 0xFFA7E2E6 into a valid instruction?",
        "opt_text": "",
        "options": [
        {
            id: 1,
            "body": "lui $at, 0xE2E6 > ori $at, $at, 0xFFA7 > ori $s4, $s2, $at",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 2,
            "body": " lui $at, 0xFFA7 > andi $at, $at, E2E6 > ori $s4, $s2, $at",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 3,
            "body": "lui $at, 0xFFA7 > ori $at, $at, 0xE2E > ori $s4, $s2, $at",
            "is_correct": True,
            "justification": "",
        },
        {
            id: 4,
            "body": "lui $at, 0xFFA7 > ori $s4, $s2, $at",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 5,
            "body": "ui $at, 0xFFA7 > andi $at, $at, 0xE2E > andi $s4, $s2, $at",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 6,
            "body": "None of the above",
            "is_correct": False,
            "justification": "",
        },
    ],
    },
    User.objects.get(id=1),
    3,
    )

    new_quiz(
        {
            "tags": ["ES"],
            "body": "What does the architecture of a project help define?",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "Unit tests",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 2,
                    "body": "Functional tests",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 3,
                    "body": "Probable risks",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 4,
                    "body": "Quality attributes",
                    "is_correct": True,
                    "justification": "",
                },
                {
                    id: 5,
                    "body": "All of the above",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 6,
                    "body": "None of the above",
                    "is_correct": False,
                    "justification": "",
                },
            ],
        },
        User.objects.get(id=1),
        4,
    )

    new_quiz(
        {
            "tags": ["COMP"],
            "body": "When is a grammar said to be ambiguous?",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "When the same non terminal symbol is used in more than one production rule",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 2,
                    "body": "When it’s recursive",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 3,
                    "body": "When it’s context free",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 4,
                    "body": "When the same input can be accepted by more than one derivation tree",
                    "is_correct": True,
                    "justification": "",
                },
                {
                    id: 5,
                    "body": "All of the above",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 6,
                    "body": "None of the above",
                    "is_correct": False,
                    "justification": "",
                },
            ],
        },
        User.objects.get(id=1),
        1,
    )

    new_quiz(
        {
            "tags": ["BD"],
            "body": "What is the function of a primary key?",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "Connecting two registers",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 2,
                    "body": "Identifying a table",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 3,
                    "body": "Opening a door",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 4,
                    "body": "Uniquely identifying a register",
                    "is_correct": True,
                    "justification": "",
                },
                {
                    id: 5,
                    "body": "All of the above",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 6,
                    "body": "None of the above",
                    "is_correct": False,
                    "justification": "",
                },
            ],
        },
        User.objects.get(id=1),
        4,
    )
    new_quiz(
    {
        "tags": ["POO"],
        "body": "What is the primary purpose of the 'Encapsulation' principle in Object-Oriented Programming?",
        "opt_text": "",
        "options": [
            {
                "id": 1,
                "body": "To enhance performance by grouping similar tasks.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 2,
                "body": "To ensure that object data is accessible only through its methods.",
                "is_correct": True,
                "justification": "",
            },
            {
                "id": 3,
                "body": "To make code easier to debug.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 4,
                "body": "To allow objects to be reused in different programs.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 5,
                "body": "To facilitate parallel development of features.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 6,
                "body": "To increase the security of the application.",
                "is_correct": False,
                "justification": "",
            },
        ],
    },
    User.objects.get(id=1),
    3,
)
    new_quiz(
        {
        "tags": ["RC"],
        "body": "What is the primary function of the Transmission Control Protocol (TCP) in the TCP/IP model?",
        "opt_text": "",
        "options": [
            {
                "id": 1,
                "body": "Routing data packets between networks.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 2,
                "body": "Providing a reliable, ordered, and error-checked delivery of a stream of packets.",
                "is_correct": True,
                "justification": "",
            },
            {
                "id": 3,
                "body": "Defining how to establish and terminate network sessions.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 4,
                "body": "Encrypting and securing data transmission.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 5,
                "body": "Assigning IP addresses to devices on a network.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 6,
                "body": "Compressing data for efficient transmission.",
                "is_correct": False,
                "justification": "",
            },
        ],
    },
    User.objects.get(id=1),
    4,
)
    new_quiz(
        {
        "tags": ["SO"],
        "body": "What is the primary function of a kernel in an operating system?",
        "opt_text": "",
        "options": [
            {
                "id": 1,
                "body": "Managing the computer's hardware and system resources.",
                "is_correct": True,
                "justification": "",
            },
            {
                "id": 2,
                "body": "Providing a user interface for easier interaction with the system.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 3,
                "body": "Installing and managing software applications.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 4,
                "body": "Protecting the system from viruses and malware.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 5,
                "body": "Optimizing the computer's performance by defragmenting the hard drive.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 6,
                "body": "Managing network connections and internet data transfer.",
                "is_correct": False,
                "justification": "",
            },
        ],
    },
    User.objects.get(id=1),
    4,
    )

    new_quiz(
        {
        "tags": ["COMP"],
        "body": "Which of the following options best describes a lexical analyzer?",
        "opt_text": "",
        "options": [
            {
                id: 1,
                "body": "A lexical analyzer is a part of the compiler that transforms a sequence of characters into a sequence of tokens. Each token is a meaningful unit of the program, such as a keyword, an identifier, an operator, or a delimiter.",
                "is_correct": True,
                "justification": "This option is correct because a lexical analyzer is a part of the compiler that transforms a sequence of characters into a sequence of tokens.",
            },
            {
                id: 2,
                "body": "“A lexical analyzer is a tool that translates source code directly into machine code.",
                "is_correct": False,
                "justification": "This option is incorrect because a lexical analyzer does not translate source code directly into machine code. This task is performed by other parts of the compiler.",
            },
            {
                id: 3,
                "body": "A lexical analyzer is a tool that checks the syntactic correctness of a program.",
                "is_correct": False,
                "justification": "This option is incorrect because it does not check the syntactic correctness of a program. This task is performed by other parts of the compiler.",
                },
                {
                id: 4,
                "body": "A lexical analyzer is a tool that optimizes the source code to improve the performance of the program.",
                "is_correct": False,
                "justification": "This option is incorrect because it does not optimize the source code to improve the performance of the program. This task is performed by other parts of the compiler.",
            },
            {
                id: 5,
                "body": "A lexical analyzer is a tool that corrects programming errors.",
                "is_correct": False,
                "justification": "This option is incorrect because a lexical analyzer does not correct programming errors. It only transforms a sequence of characters into tokens. Error detection and correction are usually performed by other parts of the compiler.",
                },
            {
                id: 6,
                "body": "A lexical analyzer is a tool that generates graphs from data.",
                "is_correct": False,
                "justification": "This option is incorrect because a lexical analyzer has nothing to do with generating graphs from data. It is a part of the compiler that transforms a sequence of characters into a sequence of tokens.",
            },
        ],
    },
    User.objects.get(id=1),
    4,
    ) 
    new_quiz(
        {
        "tags": ["SI"],
        "body": "Which of the following options best describes strategic analysis?",
        "opt_text": "",
        "options": [
            {
                id: 1,
                "body": "Strategic analysis is a process that involves only the evaluation of a company’s internal strengths and weaknesses.",
                "is_correct": False,
                "justification": "This option is incorrect because strategic analysis is not limited to only evaluating the internal environment.",
            },
            {
                id: 2,
                "body": "Strategic analysis is a process that involves researching the business environment to create a strategy. This includes evaluating the external environment (such as competitors, market, and industry trends) and the internal environment (such as the company’s resources and capabilities).",
                "is_correct": True,
                "justification": "This option is correct because strategic analysis involves evaluating both the internal and external environment of a company to create an effective strategy.",
            },
            {
                id: 3,
                "body": "Strategic analysis is a process that involves only the evaluation of a company’s external environment.",
                "is_correct": False,
                "justification": "This option is incorrect because strategic analysis is not limited to only evaluating the external environment.",
            },
            {
                id: 4,
                "body": "“Strategic analysis is a process that involves evaluating a company’s financial situation.",
                "is_correct": False,
                "justification": "",
            },
            {
                id: 5,
                "body": "A análise estratégica é um processo que envolve a avaliação do desempenho dos funcionários de uma empresa.",
                "is_correct": False,
                "justification": "This option is incorrect because strategic analysis is not limited to evaluating a company’s financial situation. It involves evaluating both the internal and external environment of a company, including but not limited to competition, market, industry trends, resources, and capabilities of the company.",
            },
            {
                id: 6,
                "body": "Strategic analysis is a process that involves evaluating the environmental impact of a company’s operations.",
                "is_correct": False,
                "justification": "This option is incorrect because, although sustainability may be an important part of a company’s strategy, strategic analysis as a whole is not limited to evaluating the environmental impact of a company’s operations. It involves a broader evaluation of the competitive environment and the internal situation of an organization.",
            },
        ],
    },
    User.objects.get(id=1),
    3,
    ) 
    new_quiz(
        {
        "tags": ["IPRP"],
        "body": "Which of the following options best describes the difference between lists and dictionaries in Python?",
        "opt_text": "",
        "options": [
            {
                id: 1,
                "body": "Lists and dictionaries in Python are basically the same thing, both are used to store collections of items.",
                "is_correct": False,
                "justification": "This option is incorrect because lists and dictionaries in Python have different uses and properties.",
            },
            {
                id: 2,
                "body": "Python lists can only store items of a single type. Python dictionaries can store items of various types.",
                "is_correct": False,
                "justification": "This option is incorrect because both lists and dictionaries can store items of various types.",
            },
            {
                id: 3,
                "body": "Python lists are used to store multiple values in a single variable. Python dictionaries cannot store multiple values.",
                "is_correct": False,
                "justification": "This option is incorrect because both lists and dictionaries can store multiple values.",
            },
            {
                id: 4,
                "body": "Python lists are an ordered collection of items that can be of any type. Python dictionaries are an unordered collection of key-value pairs.",
                "is_correct": True,
                "justification": "This option is correct, as Python lists are an ordered collection of items that can be of any type. Python dictionaries are an unordered collection of key-value pairs.",
            },
            {
                id: 5,
                "body": "Python lists are used to store numerical data, while Python dictionaries are used to store text data.",
                "is_correct": False,
                "justification": "This option is incorrect because both lists and dictionaries in Python can store various types of data, including numbers and text.",
            },
            {
                id: 6,
                "body": "Python lists cannot be changed after creation, while Python dictionaries can be changed after creation.",
                "is_correct": False,
                "justification": "This option is incorrect because Python lists are mutable, which means you can change their elements after creation.",
            },
        ],
    },
    User.objects.get(id=1),
    4,
    )
    new_quiz(
    {
        "tags": ["AC"],
        "body": "From the instructions below, which is the TAL (true assembly language) instruction.",
        "opt_text": "",
        "options": [
        {
            id: 1,
            "body": "andi $4,$5,0x0000FF00",
            "is_correct": True,
            "justification": "",
        },
        {
            id: 2,
            "body": "mul $a0, $t0, $t1",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 3,
            "body": "bge $t1, $t2, salto",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 4,
            "body": "ori $4, $5, 0x30002024",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 5,
            "body": "ori $4, $5, 0x01000030",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 6,
            "body": "None of the above",
            "is_correct": False,
            "justification": "",
        },
    ],
    },
    User.objects.get(id=1),
    2,
    )
    new_quiz(
        {
        "tags": ["AC"],
        "body": "In a program written in C and assembly, which of the following commands are valid to generate an executable, named 'exe'.",
        "opt_text": "",
        "options": [
            {
                id: 1,
                "body": "gcc main.c func.s -O exe",
                "is_correct": False,
                "justification": "",
            },
            {
                id: 2,
                "body": "gcc -c exe main.c func.s",
                "is_correct": False,
                "justification": "",
            },
            {
                id: 3,
                "body": "gcc main.c func.s -o exe",
                "is_correct": True,
                "justification": "",
            },
            {
                id: 4,
                "body": "gcc -c main.c func.s exe",
                "is_correct": False,
                "justification": "",
            },
            {
                id: 5,
                "body": "./exe",
                "is_correct": False,
                "justification": "",
            },
            {
                id: 6,
                "body": "None of the above",
                "is_correct": False,
                "justification": "",
            },
        ],
        },
    User.objects.get(id=1),
    2,
    )

    new_quiz(
    {
        "tags": ["AC"],
        "body": "The execution of the instruction addi $sp, $sp, -16 written in MIPS assembly enables:",
        "opt_text": "",
        "options": [
            {
                id: 1,
                "body": "Reserve space on the stack corresponding to 16 words",
                "is_correct": False,
                "justification": "",
            },
            {
                id: 2,
                "body": "Free space on the stack corresponding to 16 words",
                "is_correct": False,
                "justification": "",
            },
            {
                id: 3,
                "body": "Reserve space on the stack corresponding to 4 wordse",
                "is_correct": True,
                "justification": "",
            },
            {
                id: 4,
                "body": "Free space on the stack corresponding to 4 words",
                "is_correct": False,
                "justification": "",
            },
            {
                id: 5,
                "body": "All of the above",
                "is_correct": False,
                "justification": "",
            },
            {
                id: 6,
                "body": "None of the above",
                "is_correct": False,
                "justification": "",
            },
        ],
    },
    User.objects.get(id=1),
    2,
    )
    new_quiz(
{
    "tags": ["PPP"],
    "body": "When declaring a pointer type variable in C, how many bytes are pre allocated?",
    "opt_text": "",
    "options": [
        {
            id: 1,
            "body": "2 bytes",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 2,
            "body": "4 bytes",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 3,
            "body": "8 bytes",
            "is_correct": True,
            "justification": "",
        },
        {
            id: 4,
            "body": "16 bytes",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 5,
            "body": "No memory is pre allocated; we must use malloc() for that purpose",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 6,
            "body": "Pointers are a construct made by pointer factories to sell more pointers",
            "is_correct": False,
            "justification": "",
        },
    ]
},
User.objects.get(id=1),
4,
)
    new_quiz(
{
    "tags": ["RC"],
    "body": "Which of the following is the IPv4 adress reserved for Multicast DNS, assigned by the Internet Assigned Numbers Authority(IANA)?",
    "opt_text": "",
    "options": [
        {
            id: 1,
            "body": "224.0.1.129",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 2,
            "body": "224.0.0.102",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 3,
            "body": "224.0.0.2",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 4,
            "body": "224.0.1.39",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 5,
            "body": "224.0.0.251",
            "is_correct": True,
            "justification": "",
        },
        {
            id: 6,
            "body": "None of the above",
            "is_correct": False,
            "justification": "",
        },
    ]
},
User.objects.get(id=1),
4,
)
    new_quiz(
{
    "tags": ["POO"],
    "body": "Which of the following is not a principle of Object-Oriented Programing",
    "opt_text": "",
    "options": [
        {
            id: 1,
            "body": "Modularity",
            "is_correct": True,
            "justification": "",
        },
        {
            id: 2,
            "body": "Abstraction",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 3,
            "body": "Polymorphism",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 4,
            "body": "Encapsulation",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 5,
            "body": "Inheritance",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 6,
            "body": "All of the above",
            "is_correct": False,
            "justification": "",
        },
    ]
},
User.objects.get(id=1),
4,
)
    new_quiz(
        {
            "tags": ["SO"],
            "body": "Consider a system with 512MB of physical memory and 1GB of virtual memory that uses pagination. The number of pages occupies the 20 most significant bits of the logical address. What is the maximum number of pages per process?",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "2^5 pages",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 2,
                    "body": "2^19 pages",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 3,
                    "body": "2^10 pages",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 4,
                    "body": "2^20 pages",
                    "is_correct": True,
                    "justification": "",
                },
                {
                    id: 5,
                    "body": "2^50 pages",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 6,
                    "body": "None of the above",
                    "is_correct": False,
                    "justification": "",
                },
            ],
        },
        User.objects.get(id=1),
        4,
    )

    new_quiz(
        {
            "tags": ["BD"],
            "body": "Which SQL operation is used to add data to an existing table in a relational database?",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "UPDATE",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 2,
                    "body": "INSERT",
                    "is_correct": True,
                    "justification": "",
                },
                {
                    id: 3,
                    "body": "ADD",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 4,
                    "body": "CREATE",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 5,
                    "body": "ALTER",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 6,
                    "body": "DELETE",
                    "is_correct": False,
                    "justification": "",
                },
            ],
        },
        User.objects.get(id=1),
        4,
    )

    new_quiz(
        {
            "tags": ["PPP"],
            "body": "Considering: int x = 10; int *ptr = &x; printf(\"%d\n\", *ptr); What will the output be?",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "Compilation error",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 2,
                    "body": "The address of the variable x",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 3,
                    "body": "The value of the variable x",
                    "is_correct": True,
                    "justification": "",
                },
                {
                    id: 4,
                    "body": "The memory size of the variable x",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 5,
                    "body": "A random value",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 6,
                    "body": "Segmentation fault",
                    "is_correct": False,
                    "justification": "",
                },
            ],
        },
        User.objects.get(id=1),
        4,
    )




    new_quiz(
        {
            "tags": ["BD"],
            "body": "What does the following query return? SELECT AVG(Salary) FROM Employees WHERE Department = 'Finance';",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "The query retrieves the total salary of all employees in the 'Finance' department",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 2,
                    "body": "The query calculates the average salary of employees in the 'Finance' department",
                    "is_correct": True,
                    "justification": "",
                },
                {
                    id: 3,
                    "body": "The query updates the salary of employees in the 'Finance' department",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 4,
                    "body": "The query deletes all records of employees in the 'Finance' department",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 5,
                    "body": "The query inserts a new employee into the 'Finance' department",
                    "is_correct": False,
                    "justification": "",
                },
                {
                    id: 6,
                    "body": "The query retrieves the names of employees in the 'Finance' department",
                    "is_correct": False,
                    "justification": "",
                },
            ],
        },
        User.objects.get(id=2),
        4,
    )

    new_quiz(
    {
        "tags": ["TC"],
        "body": "In the context of formal languages and grammars, what is the primary purpose of terminal symbols in a context-free grammar (CFG)?",
        "opt_text": "",
        "options": [
            {
                "id": 1,
                "body": "Terminal symbols define the alphabet of the language.",
                "is_correct": True,
                "justification": "",
            },
            {
                "id": 2,
                "body": "Terminal symbols specify the production rules of the language.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 3,
                "body": "Terminal symbols generate the strings of the language by rewriting non-terminal symbols.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 4,
                "body": "Terminal symbols determine the regularity of the language.",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 5,
                "body": "All of the above",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 6,
                "body": "None of the above",
                "is_correct": False,
                "justification": "",
            },
        ],
    },
    User.objects.get(id=2),
    4,
)

    new_quiz(
    {
        "tags": ["RC"],
        "body": "Which of the following is NOT typically considered one of the primary layers in the model for computer networks?",
        "opt_text": "",
        "options": [
            {
                "id": 1,
                "body": "Physical Layer",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 2,
                "body": "Transport Layer",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 3,
                "body": "Application Layer",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 4,
                "body": "Logic Layer",
                "is_correct": True,
                "justification": "",
            },
            {
                "id": 5,
                "body": "Data Link Layer",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 6,
                "body": "Network Layer",
                "is_correct": False,
                "justification": "",
            },
        ],
    },
    User.objects.get(id=2),
    4,
)

    new_quiz(
    {
        "tags": ["RC"],
        "body": "In the context of computer networks and communication, the Transmission Control Protocol (TCP) operates at which layer?",
        "opt_text": "",
        "options": [
            {
                "id": 1,
                "body": "Physical Layer",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 2,
                "body": "Data Link Layer",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 3,
                "body": "Network Layer",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 4,
                "body": "Transport Layer",
                "is_correct": True,
                "justification": "",
            },
            {
                "id": 5,
                "body": "Session Layer",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 6,
                "body": "Application Layer",
                "is_correct": False,
                "justification": "",
            },
        ],
    },
    User.objects.get(id=3),
    4,
)

    new_quiz(
    {
        "tags": ["TC"],
        "body": "What is a key difference between non-deterministic finite automata (NFA) and deterministic finite automata (DFA)?",
        "opt_text": "",
        "options": [
            {
                "id": 1,
                "body": "NFAs always have more states than DFAs",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 2,
                "body": "DFAs can recognize regular languages, while NFAs cannot",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 3,
                "body": "NFAs and DFAs have the same expressive power and can recognize the same set of languages",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 4,
                "body": "NFAs require a stack for processing, while DFAs do not",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 5,
                "body": "NFAs are used for recognizing context-free languages, while DFAs are used for regular languages",
                "is_correct": False,
                "justification": "",
            },
            {
                "id": 6,
                "body": "NFAs can have multiple transitions for a given input symbol, while DFAs have a single transition",
                "is_correct": True,
                "justification": "",
            },
        ],
    },
    User.objects.get(id=3),
    3,
)

    new_quiz({
        "tags": ["SO"],
        "body": "In the context of O.S. we say that exists trashing when: ",
        "opt_text": "",
        "options": [
            {
                id: 1,
                "body": "We are playing with a trash talker.",
                "is_correct": False,
                "justification": "This option is unrelated to the concept of trashing in the context of operating systems.",
            },
            {
                id: 2,
                "body": "The CPU is overheating.",
                "is_correct": False,
                "justification": "Trashing in the context of an operating system refers to a specific memory management issue, not CPU overheating.",
            },
            {
                id: 3,
                "body": "The O.S. uses a segmentation system to allocate RAM for processes and has a low demand for memory.",
                "is_correct": False,
                "justification": "Trashing depends on the scheduler and is related to the demand for memory, which may vary based on the specific characteristics of the workload and the segmentation system. While a low demand for memory might reduce the likelihood of trashing, it's not the only factor. The scheduler's behavior and the nature of processes can influence whether trashing occurs.",
            },
            {
                id: 4,
                "body": "The O.S. uses a paging system, and there is excessive page swapping.",
                "is_correct": True,
                "justification": "Trashing can also occur in a paging system when there is excessive page swapping, leading to performance degradation.",
            },
            {
                id: 5,
                "body": "The O.S. is undergoing a routine update.",
                "is_correct": False,
                "justification": "Trashing is not related to routine software updates; it pertains to memory management problems in the operating system.",
            },
            {
                id: 6,
                "body": "The hard drive is almost full.",
                "is_correct": False,
                "justification": "Trashing is primarily associated with memory management issues, not the storage capacity of the hard drive.",
            },
        ],
    },
    User.objects.get(id=3),
    4,
)

    new_quiz(
{
    "tags": ["BD"],
    "body": "Among the instructions below, which is a valid SQL statement?",
    "opt_text": "",
    "options": [
        {
            "id": 1,
            "body": "SELECT name FROM customers WHERE age > 25",
            "is_correct": True,
            "justification": "",
        },
        {
            "id": 2,
            "body": "MULTIPLY salary BY 1.1 WHERE department = 'IT'",
            "is_correct": False,
            "justification": "",
        },
        {
            "id": 3,
            "body": "COMPARE name = 'John' AND surname = 'Smith'",
            "is_correct": False,
            "justification": "",
        },
        {
            "id": 4,
            "body": "UPDATE products SET quantity = quantity - 1 WHERE id = 102",
            "is_correct": False,
            "justification": "",
        },
        {
            "id": 5,
            "body": "INSERT INTO employees (id, name, position) VALUES (101, 'Ana', 'Analyst')",
            "is_correct": False,
            "justification": "",
        },
        {
            "id": 6,
            "body": "None of the above",
            "is_correct": False,
            "justification": "",
        },
    ],
},
User.objects.get(id=2),
4,
)

    new_quiz(
{
    "tags": ["SO"],
    "body": "Which of the following is an essential component of an operating system?",
    "opt_text": "",
    "options": [
        {
            "id": 1,
            "body": "Kernel",
            "is_correct": True,
            "justification": "",
        },
        {
            "id": 2,
            "body": "Compiler",
            "is_correct": False,
            "justification": "",
        },
        {
            "id": 3,
            "body": "Debugger",
            "is_correct": False,
            "justification": "",
        },
        {
            "id": 4,
            "body": "Router",
            "is_correct": False,
            "justification": "",
        },
        {
            "id": 5,
            "body": "Database",
            "is_correct": False,
            "justification": "",
        },
        {
            "id": 6,
            "body": "None of the above",
            "is_correct": False,
            "justification": "",
        },
    ],
},
User.objects.get(id=2),
4,
)

    new_quiz(
{
    "tags": ["IPRP"],
    "body": "In Python, what does the zip() function do?",
    "opt_text": "",
    "options": [
        {
            id: 1,
            "body": "Combines two lists into a single list.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 2,
            "body": "Unzips a compressed file.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 3,
            "body": "Creates an iterator that aggregates elements from multiple iterable objects.",
            "is_correct": True,
            "justification": "",
        },
        {
            id: 4,
            "body": "Sorts a list in ascending order.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 5,
            "body": "Converts a string to uppercase.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 6,
            "body": "Checks if a file exists in the specified path.",
            "is_correct": False,
            "justification": "",
        },
    ]
},
User.objects.get(id=2),
4,
)

    new_quiz(
{
    "tags": ["PPP"],
    "body": "What is the purpose of the static keyword in C",
    "opt_text": "",
    "options": [
        {
            id: 1,
            "body": "Declares a variable that is visible only within the current function.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 2,
            "body": "Indicates that a variable will be modified by multiple threads.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 3,
            "body": "Specifies that a function should be compiled to machine code.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 4,
            "body": "Allocates memory for a variable on the heap.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 5,
            "body": "Declares a global variable that can be accessed from other source files.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 6,
            "body": "Specifies that a variable retains its value between function calls.",
            "is_correct": True,
            "justification": "",
        },
    ]
},
User.objects.get(id=3),
3,
)

    new_quiz(
{
    "tags": ["SO"],
    "body": "What does the sudo command in Linux allow a user to do?",
    "opt_text": "",
    "options": [
        {
            id: 1,
            "body": "Install new software packages.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 2,
            "body": "Create a new user account.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 3,
            "body": "Delete files and directories.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 4,
            "body": "Change the system hostname.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 5,
            "body": "Access the system as the root user.",
            "is_correct": True,
            "justification": "",
        },
        {
            id: 6,
            "body": "Modify file permissions.",
            "is_correct": False,
            "justification": "",
        },
    ]
},
User.objects.get(id=3),
3,
)

new_quiz(
{
    "tags": ["IPRP"],
    "body": "What is an algorithm?",
    "opt_text": "",
    "options": [
        {
            id: 1,
            "body": "A computer program.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 2,
            "body": "A data input device.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 3,
            "body": "A data output device.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 4,
            "body": "A data storage device.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 5,
            "body": "A sequence of instructions that specifies how to perform a task.",
            "is_correct": True,
            "justification": "",
        },
        {
            id: 6,
            "body": " A data processing device.",
            "is_correct": False,
            "justification": "",
        },
    ]
},
User.objects.get(id=3),
4,
)


new_quiz(
{
    "tags": ["BD"],
    "body": "What is the main purpose of concurrency control in a database system?",
    "opt_text": "",
    "options": [
        {
            id: 1,
            "body": "Improve data security.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 2,
            "body": "Increase the efficiency of consultations.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 3,
            "body": "Ensure data consistency.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 4,
            "body": "Reduce storage space.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 5,
            "body": "Facilitate the recovery of lost data.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 6,
            "body": "Ensure that multiple competing transactions do not cause inconsistent results.",
            "is_correct": True,
            "justification": "",
        },
    ]
},
User.objects.get(id=2),
4,
)

new_quiz(
{
    "tags": ["ES"],
    "body": "What is the main objective of unit testing in Software Engineering?",
    "opt_text": "",
    "options": [
        {
            id: 1,
            "body": "Check the functionality of the system as a whole.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 2,
            "body": "Ensure that the code is free from compilation errors.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 3,
            "body": "Test the integration between different modules.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 4,
            "body": "Identify flaws in software design.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 5,
            "body": "Evaluate the general performance of the application.",
            "is_correct": False,
            "justification": "",
        },
        {
            id: 6,
            "body": "Validate the individual and isolated behavior of code units, such as functions or methods.",
            "is_correct": True,
            "justification": "",
        },
    ]
},
User.objects.get(id=2),
4,
)
