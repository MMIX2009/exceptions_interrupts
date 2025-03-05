import streamlit as st

# Title of the app
st.title("Exceptions and Interrupts Quiz")
st.write("Master the Flow of Control: Test Your Knowledge on Exceptions and Interrupts! 🚀")

# Initialize session state variables if they don’t exist
if "score" not in st.session_state:
    st.session_state.score = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answer_submitted" not in st.session_state:
    st.session_state.answer_submitted = False

# Questions and answers

quiz = [
# Exceptions and Interrupts
{"question": "What is the main difference between an exception and an interrupt?",
 "options": ["Exceptions come from external devices, interrupts arise in the CPU", "Exceptions arise within the CPU, interrupts come from external devices", "Both refer to the same event", "Exceptions occur only in software, interrupts only in hardware"],
 "answer": "Exceptions arise within the CPU, interrupts come from external devices"},

{"question": "Which of the following is an example of an exception?",
 "options": ["Undefined opcode", "Keyboard input", "Disk I/O completion", "Timer expiration"],
 "answer": "Undefined opcode"},

{"question": "Which register in MIPS stores the PC of the offending instruction?",
 "options": ["EPC", "Cause", "Status", "Stack Pointer"],
 "answer": "EPC"},

# Handling Exceptions
{"question": "What action does the system take when an exception occurs?",
 "options": ["Ignores the instruction", "Jumps to the exception handler", "Restarts the program", "Halts execution permanently"],
 "answer": "Jumps to the exception handler"},

{"question": "What does the Cause register in MIPS indicate?",
 "options": ["Current instruction", "Type of exception", "Memory address", "Stack pointer value"],
 "answer": "Type of exception"},

# Vectored Interrupts
{"question": "How do vectored interrupts determine the handler address?",
 "options": ["Using a table of predefined addresses", "From a global exception handler", "From the instruction cache", "Based on user input"],
 "answer": "Using a table of predefined addresses"},

{"question": "Why are vectored interrupts used?",
 "options": ["To avoid handling all exceptions in a single handler", "To slow down execution", "To disable pipeline processing", "To replace virtual memory"],
 "answer": "To avoid handling all exceptions in a single handler"},

# Exceptions in a Pipeline
{"question": "How does an exception affect a pipelined processor?",
 "options": ["Flushes the pipeline and transfers control to a handler", "Ignores the instruction", "Pauses execution for one cycle", "Increases clock speed"],
 "answer": "Flushes the pipeline and transfers control to a handler"},

{"question": "What must be done before handling an exception in a pipeline?",
 "options": ["Flush the pipeline", "Increase clock cycles", "Restart the CPU", "Disable all registers"],
 "answer": "Flush the pipeline"},

# Restartable Exceptions
{"question": "Why are some exceptions considered restartable?",
 "options": ["They can be refetched and executed from scratch", "They only occur in the cache", "They never modify registers", "They do not impact memory"],
 "answer": "They can be refetched and executed from scratch"},

{"question": "Where is the PC stored when handling an exception?",
 "options": ["EPC register", "Cache memory", "Interrupt table", "General purpose register"],
 "answer": "EPC register"},

# Multiple Exceptions
{"question": "How does a CPU handle multiple exceptions occurring at once?",
 "options": ["Processes the earliest instruction first", "Handles all at the same time", "Ignores all but one", "Restarts execution from the beginning"],
 "answer": "Processes the earliest instruction first"},

{"question": "Why is maintaining precise exceptions difficult in complex pipelines?",
 "options": ["Out-of-order execution", "Too many registers", "Memory access issues", "Lack of caching"],
 "answer": "Out-of-order execution"},

# Imprecise Exceptions
{"question": "What is an imprecise exception?",
 "options": ["An exception where the exact causing instruction is not known", "A rare type of hardware error", "An interrupt from external devices", "An error that can be ignored safely"],
 "answer": "An exception where the exact causing instruction is not known"},

{"question": "How do imprecise exceptions simplify hardware design?",
 "options": ["By saving state and letting software determine the cause", "By increasing memory usage", "By disabling virtual memory", "By ignoring exception handling"],
 "answer": "By saving state and letting software determine the cause"},

{"question": "Why are imprecise exceptions challenging for software?",
 "options": ["They require manual completion of some instructions", "They reduce CPU performance", "They make cache coherence difficult", "They slow down I/O operations"],
 "answer": "They require manual completion of some instructions"},

# Exception Handling Example
{"question": "In MIPS, what address does an exception handler jump to?",
 "options": ["8000 00180", "0000 0000", "FFFF FFFF", "C000 0020"],
 "answer": "8000 00180"},

{"question": "Which of the following is NOT a possible action by an exception handler?",
 "options": ["Terminate the program", "Return to execution", "Ignore the exception", "Restart the pipeline"],
 "answer": "Ignore the exception"}
]

# The above list contains 20 MCQ questions covering exceptions, interrupts, and pipeline handling.

# Display the current question
current_question = quiz[st.session_state.question_index]
st.write(f"**Question {st.session_state.question_index + 1}: {current_question['question']}**")

# Multiple-choice options
selected_option = st.radio("Select your answer:", current_question["options"], key=f"question_{st.session_state.question_index}")

# Submit button to evaluate the selected answer
if st.button("Submit Answer") and not st.session_state.answer_submitted:
    if selected_option == current_question["answer"]:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error(f"Incorrect. The correct answer is: {current_question['answer']}")
    st.session_state.answer_submitted = True

# Next button (enabled only after an answer is submitted)
if st.session_state.answer_submitted:
    if st.button("Next Question"):
        if st.session_state.question_index < len(quiz) - 1:
            st.session_state.question_index += 1
            st.session_state.answer_submitted = False
            # Force rerun to display the next question immediately
            st.rerun()
        else:
            st.write("### Quiz Completed!")
            st.write(f"Your final score is {st.session_state.score}/{len(quiz)}")
            st.session_state.question_index = 0
            st.session_state.score = 0
            st.session_state.answer_submitted = False

st.write(f"**Current Score:** {st.session_state.score}")
