# Documentation Template for Legacy Code Systems

---

## FUNCTION: [Function Identifier] - [Function Name]

**Purpose:**  
[Briefly describe the purpose of the program.]

**Description:**  
[A short description of what the program does.]

---

## DETAILED DESCRIPTION

**Program Overview:**  
[Provide a high-level overview of the program's functionality.]

**Key Features/Functionality:**

- [Feature 1]
- [Feature 2]
- [Feature 3]

---

## FIELD MAPPING AND LOGIC

**Instructions:** For each field in the output report or file, specify the source of the data, any transformation or calculations applied, and any relevant business rules. The field can be defined in the input files and based on the
headers of that file you can derive the functional description of that field.
Below is a guide on how to document each field.

| No  | Field Name         | Source Table and Column        | Transformation or Business Logic                                                                 |
| --- | ------------------ | ------------------------------ | ------------------------------------------------------------------------------------------------ |
| 1   | **[Field Name 1]** | **[Table Name].[Column Name]** | [Describe how the data is transformed, e.g., format changes, concatenations, calculations, etc.] |
| 2   | **[Field Name 2]** | **[Table Name].[Column Name]** | [Include details about any conditional logic or additional processing for this field.]           |
| 3   | **[Field Name 3]** | **[Table Name].[Column Name]** | [Mention any special cases or exceptions related to this field.]                                 |

**Additional Notes:**

- **Field Name:** The name of the variable used in the program followed by a tunctional description of the field
  based on the usage of the field in the program or the source of the variable.
- **Source Table:** Specify the database table or input file from which the field data is retrieved.
- **Source Column:** Specify the exact column(s) from which the data is sourced.
- **Transformation Logic:** Describe any transformations or business rules applied to the data before it is included in the output.
- **Special Cases:** Note any conditions under which the data might vary (e.g., exceptions, null values).

---

## PROCESS FLOW

**Main Procedure:**

1. **Initialization:**  
   [Describe the initialization steps taken by the program.]
   [Example: `PROC_INIT` initializes various parameters.]

2. **Data Preparation:**

   - **Input File Structure:**  
     [Describe the important fields of the input file, if applicable.]

   - **SQL Declarations and Queries:**  
     [Describe the SQL queries and cursor operations used.]

3. **Main Processing Loop:**  
   [Explain how the program processes each record, including any loops or conditional logic.]

4. **File Writing:**

   - **Output File Structure:**  
     [Describe the logic for creating the output file, if applicable.]

5. **Finalization:**
   - [Describe the final steps the program takes before completion.]

---

## PARAMETERS AND RERUN LOGIC

**Parameters:**  
[List and describe any parameters used in the program.]

**Rerun Logic:**  
[Explain how the program handles reruns, including how parameters are managed.]

---

## ERROR HANDLING

**Error Handling Mechanisms:**

- [Describe how errors are detected and managed.]
- [Example: Issues with converting records to IBAN format trigger specific messages.]

---

## SPECIAL CASES

**Handling of Edge Cases:**  
[Describe any specific conditions under which the program behaves differently or requires special handling. For example, this could include scenarios where certain input data is missing, invalid, or requires alternative processing.]

**Special Calculations or Logic:**

- **Date Calculations:**  
  [Describe any specific date-related calculations or logic used in the program. This could include determining reporting periods, calculating working days, or adjusting dates based on business rules.]

- **Conditional Processing:**  
  [Outline any conditional logic that alters the standard flow of the program. For example, how the program handles reruns, alternative file formats, or different data sources.]

- **Exception Handling:**  
  [Explain how the program manages exceptions or unusual conditions that deviate from the normal processing path. Include details on how errors are logged or reported.]

---

## SYSTEM DEPENDENCIES

**Dependencies on Other Programs/Files:**

- [List any external programs or files that this program depends on.]

**Include Files:**

- [List the include files used in the program, such as `FAIBATCH`, `FAIPL1`, etc.]

---

## OUTPUT

**Output Files:**

- **File Name:** [Name of the output file]
- **Structure:** [Detailed structure of the output file, field-by-field]

**Reporting Mechanism:**

- [Describe how the output file is handled post-creation, e.g., retrieved by OBS.]
