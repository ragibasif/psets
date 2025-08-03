/*
 * File: test_dynamic_array.c
 * Author: Ragib Asif
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 */

#include "dbg.h"
#include "dynamic_array.h"

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

void test_dynamic_array_stack_allocation( void ) {
    struct dynamic_array da;
    da_init( &da );
    assert( da.size == 0 );
    assert( da.capacity == DEFAULT_CAPACITY_SIZE );
    da_cleanup( &da );
    assert( da.size == 0 );
    assert( da.capacity == 0 );
    assert( !da.buffer );
}

void test_dynamic_array_heap_allocation( void ) {
    struct dynamic_array *da = malloc( sizeof *da );
    da_init( da );
    assert( da->size == 0 );
    assert( da->capacity == DEFAULT_CAPACITY_SIZE );
    da_cleanup( da );
    assert( da->size == 0 );
    assert( da->capacity == 0 );
    assert( !da->buffer );
    free( da );
    da = NULL;
}

void test_dynamic_array_push( void ) {
    struct dynamic_array da;
    da_init( &da );
    assert( da.size == 0 );
    assert( da.capacity == DEFAULT_CAPACITY_SIZE );

    da_push( &da, 0xff );
    assert( da.buffer[0] == 0xff );
    assert( da.size == 1 );
    da_push( &da, 0x00 );
    assert( da.buffer[1] == 0x00 );
    assert( da.size == 2 );
    da_push( &da, 0x2f );
    assert( da.buffer[2] == 0x2f );
    assert( da.size == 3 );
    da_push( &da, 0x9a );
    assert( da.buffer[3] == 0x9a );
    assert( da.size == 4 );
    da_push( &da, 0x10 );
    assert( da.buffer[4] == 0x10 );
    assert( da.size == 5 );
    da_push( &da, 0x6b );
    assert( da.buffer[5] == 0x6b );
    assert( da.size == 6 );
    assert( da.capacity == DEFAULT_CAPACITY_SIZE );

    da_cleanup( &da );
    assert( da.size == 0 );
    assert( da.capacity == 0 );
    assert( !da.buffer );
}

void test_dynamic_array_pop( void ) {
    struct dynamic_array da;
    da_init( &da );
    assert( da.size == 0 );
    assert( da.capacity == DEFAULT_CAPACITY_SIZE );

    da_push( &da, 0xff );
    assert( da.buffer[0] == 0xff );
    assert( da.size == 1 );
    da_push( &da, 0x00 );
    assert( da.buffer[1] == 0x00 );
    assert( da.size == 2 );
    da_push( &da, 0x2f );
    assert( da.buffer[2] == 0x2f );
    assert( da.size == 3 );
    da_push( &da, 0x9a );
    assert( da.buffer[3] == 0x9a );
    assert( da.size == 4 );
    da_push( &da, 0x10 );
    assert( da.buffer[4] == 0x10 );
    assert( da.size == 5 );
    da_push( &da, 0x6b );
    assert( da.buffer[5] == 0x6b );
    assert( da.size == 6 );
    assert( da.capacity == DEFAULT_CAPACITY_SIZE );

    da_pop( &da );
    assert( da.size == 5 );
    da_pop( &da );
    assert( da.size == 4 );
    da_pop( &da );
    assert( da.size == 3 );
    da_pop( &da );
    assert( da.size == 2 );
    da_pop( &da );
    assert( da.size == 1 );
    da_pop( &da );
    assert( da.size == 0 );

    assert( da.capacity == DEFAULT_CAPACITY_SIZE );

    da_cleanup( &da );
    assert( da.size == 0 );
    assert( da.capacity == 0 );
    assert( !da.buffer );
}

void test_dynamic_array_array_expansion( void ) {
    struct dynamic_array da;
    da_init( &da );
    assert( da.size == 0 );
    assert( da.capacity == DEFAULT_CAPACITY_SIZE );

    for ( size_t i = 0; i < DEFAULT_CAPACITY_SIZE * 4; i++ ) {
        da_push( &da, 1 < i );
    }

    assert( da.capacity != DEFAULT_CAPACITY_SIZE );
    assert( da.capacity == DEFAULT_CAPACITY_SIZE * 4 );

    for ( size_t i = 0; i < DEFAULT_CAPACITY_SIZE * 4; i++ ) { da_pop( &da ); }
    assert( da.capacity != DEFAULT_CAPACITY_SIZE );
    assert( da.capacity == DEFAULT_CAPACITY_SIZE * 4 );

    da_cleanup( &da );
    assert( da.size == 0 );
    assert( da.capacity == 0 );
    assert( !da.buffer );
}

void test_dynamic_array_all( void ) {
    dbg( "START" );

    test_dynamic_array_stack_allocation();
    test_dynamic_array_heap_allocation();
    test_dynamic_array_push();
    test_dynamic_array_pop();
    test_dynamic_array_array_expansion();

    dbg( "END" );
}
