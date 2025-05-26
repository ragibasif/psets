#!/bin/sh

# File: old.sh
# Author: Ragib Asif
# Email: ragib.asif30@myhunter.cuny.edu
# GitHub: https://github.com/ragibasif
# LinkedIn: https://www.linkedin.com/in/ragibasif/
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Ragib Asif

set -Ceuvx

# set -n # debugging

# Usage: ./new.sh [platform] [problem_id] [difficulty/contest] [problem_name] [language]

PLATFORM=$1        # e.g., "codeforces", "leetcode"
PROBLEM_ID=$2      # e.g., "1823A", "two_sum"
CONTEST_OR_DIFF=$3 # e.g., "1800-1999" (CF) or "easy" (LeetCode)
PROBLEM_NAME=$4    # e.g., "characteristic" (optional)
LANGUAGE=$5        # e.g., "py" or "cpp" (programming language)

# Define paths
PLATFORM_DIR="./${PLATFORM}"
CATEGORY_DIR="${PLATFORM_DIR}/${CONTEST_OR_DIFF}"
FILE_DIR="${CATEGORY_DIR}/${PROBLEM_ID}_${PROBLEM_NAME}"
FILE_PATH="${FILE_DIR}/main.${LANGUAGE}"
TEMPLATE_DIR="./templates"
TEMPLATE_FILE="${TEMPLATE_DIR}/main.${LANGUAGE}"
TEMPLATE_BUILD="${TEMPLATE_DIR}/Makefile"

# Create directory if it doesn't exist
mkdir -p "$FILE_DIR"

# Generate file with template and metadata
if [ "$LANGUAGE" = "py" ]; then
    cat >"$FILE_PATH" <<EOF
"""
# File: ${PROBLEM_ID}_${PROBLEM_NAME}.${LANGUAGE}
# Author: Ragib Asif
# Email: ragib.asif30@myhunter.cuny.edu
# GitHub: https://github.com/ragibasif
# LinkedIn: https://www.linkedin.com/in/ragibasif/
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Ragib Asif
#
# Problem: ${PROBLEM_ID} ${PROBLEM_NAME}
# Platform: ${PLATFORM}
# Contest/Difficulty: ${CONTEST_OR_DIFF}
"""
EOF
else
    cat >"$FILE_PATH" <<EOF
/*
 * File: ${PROBLEM_ID}_${PROBLEM_NAME}.${LANGUAGE}
 * Author: Ragib Asif
 * Email: ragib.asif30@myhunter.cuny.edu
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 *
 * Problem: ${PROBLEM_ID} ${PROBLEM_NAME}
 * Platform: ${PLATFORM}
 * Contest/Difficulty: ${CONTEST_OR_DIFF}
 */
EOF
    cat "$TEMPLATE_FILE" >>"$FILE_PATH"
    cp "$TEMPLATE_BUILD" "$FILE_DIR"
fi

printf '%s\n' "Success"
printf '%s\n' "Created: ${FILE_PATH}"

exit 0
