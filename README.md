# Llama.cpp API Python Integration

A simple guide to get the llama.cpp chat API up and running using Python.

## Steps to Follow

### Step 1: Clone and Run the Llama.cpp Library

First, clone the llama.cpp library from the following repository:

[llama.cpp](https://github.com/ggerganov/llama.cpp)

After cloning, navigate to the `llama.cpp` folder.

### Step 2: Run the Server

In the `llama.cpp` folder, run the server file using the command below. Make sure to edit the path to your `ggml` file accordingly:

```bash
./server -m models/13b-chat/ggml-model-q4_0.bin -c 2048
```
### Step 3: Clone the API Python Repository

After running the server, clone the Llama.cpp API Python repository:

```bash
git clone https://github.com/avinrique/Llama.cpp-api-python-
```
### Navigate to the cloned directory:
```bash
cd Llama.cpp-api-python-
```
### Copy and paste file over the parent directory
```bash
cp fetch_chatapi.py ./../
```
### Run the file
```python
python app.py
```

