<template>
   <footer>
    <div>
      <span>@2024 GameStore, все права защищены.</span>
    </div>
    <div>
      <span>Правила использования</span>
      <span>&nbsp</span>
      <span>|</span>
      <span>&nbsp</span>
      <span>Политика конфиденциальности</span>
    </div>
  </footer>
</template>

<script>
export default {
name: "Footer"
}
</script>

<style scoped>
footer {
  display: flex;
  align-content: center;
  align-items: center;
  flex-direction: row;
  flex-wrap: nowrap;
  justify-content: space-around;
  font-size: 18px;
  line-height: 27px;
  font-weight: 400;
  background-color: #0f0f0f;
  color: #999999;
  width: 100%;
  height: 10vh;
  border-top: 1px solid #262626;
  text-align: center;
  border-radius: 0 0 5px 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 999;
}
</style>
