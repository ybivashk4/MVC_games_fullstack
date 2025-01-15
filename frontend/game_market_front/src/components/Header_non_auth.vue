<template>
  <header class="header_non_auth">
    <div>GamesStore</div>
    <div><img src="../assets/profile.svg" alt=""></div>
  </header>
</template>

<script>
export default {
  name: "Header_non_auth"
}
</script>

<style scoped>
.header_non_auth {
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
</style>
