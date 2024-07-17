<script>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import axios from 'axios';

export default {
  data() {
    return {
      message: '',
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/playground/hello/');
        this.message = response.data.message;
        console.log(response.data.message);
      } catch (error) {
        console.error('Error fetching data:', error);ou 
      }
    },
  },
};

</script>

<template>
  <header>
    <img alt="Vue logo" class="" src="./assets/logo.svg" width="125" height="125" />
    


  </header>

  <main>
    <p class="font-[29px] text-sky-300"> hello</p>
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
