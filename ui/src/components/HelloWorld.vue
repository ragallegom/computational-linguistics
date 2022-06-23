<template>
  <form id="app" @submit="checkForm" action="http://localhost:8000/core/" method="post">
    <p v-if="errors.length">
      <b>Por favor, corrija el(los) siguiente(s) error(es):</b>
    <ul>
      {{ errors }}
    </ul>
    </p>
    <p>
      <label for="name">Texto</label><br>
      <input id="name" v-model="name" type="text" name="name">
    </p>
    <p>
      <input type="submit" value="Enviar">
    </p>
  </form>
  /*******************************************/
  <p>PROXIMAMENTE</p>
  <p>Subir archivo:</p>
  <input type="file" id="avatar" name="avatar" accept=".doc, .docx, .pdf">
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      message: '',
      errors: [],
      name: null
    }
  },
  methods:{
    checkForm: function (e) {
      if (this.name) {
        return true;
      }

      this.errors = [];

      if (!this.name) {
        this.errors.push('El texto es obligatorio.');
      }

      e.preventDefault();
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
