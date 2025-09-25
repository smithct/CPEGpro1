        .global main     // Entry point

main:                   // Program starts here
        MOV X0, #5       // Example: load 5 into X0
        MOV X1, #7       // Load 7 into X1
        ADD X2, X0, X1   // X2 = X0 + X1

        // Your project code will go here

        // End program
        HALT             // Stop execution
