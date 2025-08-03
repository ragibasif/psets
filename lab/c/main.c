/*
 * File: main.c
 * Author: Ragib Asif
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 */

#include "dbg.h"
#include "test_dynamic_array.h"

#include <stdio.h>
#include <stdlib.h>

int main( [[maybe_unused]] int argc, [[maybe_unused]] char **argv ) {
    dbg( "Running all tests..." );

    test_dynamic_array_all();

    dbg( "...Finished." );

    return EXIT_SUCCESS;
}
