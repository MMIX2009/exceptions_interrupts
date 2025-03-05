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
{
    "question": "What is the main difference between an exception and an interrupt?",
    "options": [
      "Both refer to the same event",
      "Exceptions arise within the CPU, interrupts come from external devices",
      "Exceptions come from external devices, interrupts arise in the CPU",
      "Exceptions occur only in software, interrupts only in hardware"
    ],
    "answer": "Exceptions arise within the CPU, interrupts come from external devices"
  },
  {
    "question": "Which of the following is an example of an exception?",
    "options": [
      "Disk I/O completion",
      "Timer expiration",
      "Undefined opcode",
      "Keyboard input"
    ],
    "answer": "Undefined opcode"
  },
  {
    "question": "Which register in MIPS stores the PC of the offending instruction?",
    "options": [
      "Cause",
      "Stack Pointer",
      "EPC",
      "Status"
    ],
    "answer": "EPC"
  },
  {
    "question": "What action does the system take when an exception occurs?",
    "options": [
      "Restarts the program",
      "Halts execution permanently",
      "Jumps to the exception handler",
      "Ignores the instruction"
    ],
    "answer": "Jumps to the exception handler"
  },
  {
    "question": "What does the Cause register in MIPS indicate?",
    "options": [
      "Memory address",
      "Type of exception",
      "Stack pointer value",
      "Current instruction"
    ],
    "answer": "Type of exception"
  },
  {
    "question": "How do vectored interrupts determine the handler address?",
    "options": [
      "Based on user input",
      "From the instruction cache",
      "Using a table of predefined addresses",
      "From a global exception handler"
    ],
    "answer": "Using a table of predefined addresses"
  },
  {
    "question": "Why are vectored interrupts used?",
    "options": [
      "To disable pipeline processing",
      "To avoid handling all exceptions in a single handler",
      "To replace virtual memory",
      "To slow down execution"
    ],
    "answer": "To avoid handling all exceptions in a single handler"
  },
  {
    "question": "How does an exception affect a pipelined processor?",
    "options": [
      "Pauses execution for one cycle",
      "Flushes the pipeline and transfers control to a handler",
      "Increases clock speed",
      "Ignores the instruction"
    ],
    "answer": "Flushes the pipeline and transfers control to a handler"
  },
  {
    "question": "What must be done before handling an exception in a pipeline?",
    "options": [
      "Increase clock cycles",
      "Disable all registers",
      "Flush the pipeline",
      "Restart the CPU"
    ],
    "answer": "Flush the pipeline"
  },
  {
    "question": "Why are some exceptions considered restartable?",
    "options": [
      "They never modify registers",
      "They can be refetched and executed from scratch",
      "They do not impact memory",
      "They only occur in the cache"
    ],
    "answer": "They can be refetched and executed from scratch"
  },
  {
    "question": "Where is the PC stored when handling an exception?",
    "options": [
      "Cache memory",
      "EPC register",
      "General purpose register",
      "Interrupt table"
    ],
    "answer": "EPC register"
  },
  {
    "question": "How does a CPU handle multiple exceptions occurring at once?",
    "options": [
      "Handles all at the same time",
      "Processes the earliest instruction first",
      "Restarts execution from the beginning",
      "Ignores all but one"
    ],
    "answer": "Processes the earliest instruction first"
  },
  {
    "question": "Why is maintaining precise exceptions difficult in complex pipelines?",
    "options": [
      "Memory access issues",
      "Lack of caching",
      "Out-of-order execution",
      "Too many registers"
    ],
    "answer": "Out-of-order execution"
  },
  {
    "question": "What is an imprecise exception?",
    "options": [
      "A rare type of hardware error",
      "An error that can be ignored safely",
      "An exception where the exact causing instruction is not known",
      "An interrupt from external devices"
    ],
    "answer": "An exception where the exact causing instruction is not known"
  },
  {
    "question": "How do imprecise exceptions simplify hardware design?",
    "options": [
      "By increasing memory usage",
      "By saving state and letting software determine the cause",
      "By ignoring exception handling",
      "By disabling virtual memory"
    ],
    "answer": "By saving state and letting software determine the cause"
  },
  {
    "question": "Why are imprecise exceptions challenging for software?",
    "options": [
      "They reduce CPU performance",
      "They require manual completion of some instructions",
      "They slow down I/O operations",
      "They make cache coherence difficult"
    ],
    "answer": "They require manual completion of some instructions"
  },
  {
    "question": "In MIPS, what address does an exception handler jump to?",
    "options": [
      "0000 0000",
      "8000 00180",
      "C000 0020",
      "FFFF FFFF"
    ],
    "answer": "8000 00180"
  },
  {
    "question": "Which of the following is NOT a possible action by an exception handler?",
    "options": [
      "Return to execution",
      "Restart the pipeline",
      "Ignore the exception",
      "Terminate the program"
    ],
    "answer": "Ignore the exception"
  },
  {
    "question": "What is the purpose of an interrupt service routine (ISR)?",
    "options": [
      "To store system logs",
      "To handle interrupts by executing specific code",
      "To disable unused memory",
      "To increase CPU performance"
    ],
    "answer": "To handle interrupts by executing specific code"
  },
  {
    "question": "Which type of interrupt occurs at predictable times?",
    "options": [
      "Software interrupt",
      "I/O interrupt",
      "Timer interrupt",
      "Hardware interrupt"
    ],
    "answer": "Timer interrupt"
  }

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
