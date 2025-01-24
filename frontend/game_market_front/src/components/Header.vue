<template>
  <header class="header">
    <div>GamesStore</div>
    <div class="search_game" style="display: flex">
      <img src="../assets/search.svg" alt="">
      <div>Поиск игры...</div>
    </div>
    <div class="header_icons">
      <div style="display: flex">
      <span>0</span>
      <img
        src="../assets/bin.svg" alt=""
        @click="redirectTo('/bin')"
      >
      </div>

      <img
        src="../assets/menu.svg" alt=""
        @click="redirectTo('/')"
      >
      <img
        src="../assets/logout.svg"
        alt=""
        @click="logout()"
      >
    </div>
  </header>
</template>

<script>
export default {
  name: "Header",
  methods: {
    redirectTo(path) {
      this.$router.push(path);
    },
    logout() {
      localStorage.removeItem('refresh');
      localStorage.removeItem('access');
      alert('Вы вышли из аккаунта');
      this.$router.push('/login');
    },
  },
}
</script>

<style scoped>
.header {
  display: flex;
  align-content: center;
  align-items: center;
  flex-direction: row;
  justify-content: space-around;
  font-size: 26px;
  line-height: 26px;
  margin-top: 3%;

  width: 100%;
}
.search_game {
  display: flex;
  justify-content: flex-start;
  align-content: center;
  align-items: center;
  color: #545454;
  width: 70vh;
  height: 6vh;
  padding-left: 2vh;
  padding-right: 2vh;
  background-color: #0F0F0F;
  border-radius: 6px;
  font-size: 18px;
}
.header_icons {
  display: flex;
  justify-content: space-between;
  font-size: 22px;
  line-height: 33px;
  font-weight: 500;
  width: 25vh;
}
</style>
