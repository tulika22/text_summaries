<template>
  <div class="container">
    <h1>Summarizer</h1>
    <p>
      Welcome to Summarizer! 
      Insert your text below to get it summarized.
    </p>

    <form id="ruleForm">
      <textarea v-model="input" form="ruleForm" rows="10" cols="40" placeholder="Provide the text here" style="width: 100%; margin-bottom: 1rem;" />

      <label for="persona">Persona: </label>
      <input
        type="text"
        style="margin: 1rem 0; width: 100%;"
        placeholder="Enter a persona"
        id="persona"
        v-model="persona"
      />
      <br/>

      <label for="selectWordCount">Word Limit </label>
      <select v-model="wordCount" id="selectWordCount" style="margin-bottom: 1rem; width: 100%;">
        <option value="50">50</option>
        <option value="100">100</option>
        <option value="150">150</option>
      </select>
      <br />

      <button style="margin-top: 0.5rem;" v-on:click.prevent="clear">Clear</button>
      <button style="margin-top: 0.5rem; margin-left: 0.5rem;" v-on:click.prevent="createSummary">Create summary</button>
    </form>

    <div v-if="output" style="margin-top: 1rem;">
      <p><strong>Output:</strong></p>
      <p>{{ output }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      input: "",
      output: "",
      persona: "Human",
      wordCount: 100
    }
  },
  methods: {
    clear() {
      this.input = ""
      this.output = ""
      this.persona = "Human"
      this.wordCount = 100
    },
    async createSummary() {
      try {
        let res = await axios.post("http://localhost:9000/summary", {
          text: this.input,
          persona: this.persona,
          wordCount: this.wordCount
        })
        console.log(res)
        this.output = res.data
      } catch (error) {
        this.output = error
      }
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: auto;
  padding: 1rem;
}

textarea {
  resize: vertical;
}

button {
  padding: 0.5rem 1rem;
  border: none;
  background-color: #007BFF;
  color: white;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>