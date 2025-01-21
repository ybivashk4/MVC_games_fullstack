<template>
  <div class="bin_card">
    <img :src="ImagePath" alt="" height="122px" width="220px">
    <div>{{game_name}}</div>
    <div class="flex-column price">
      <div>
        {{price}} Р
      </div>
      <div style="margin-left: 100%" class="change_text_color">
        Удалить
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BinCard",
  props: {
    ImagePath: {
      type: String,
      required: true
    },

    game_name: {
      type: String,
      required: true
    },
    price: {
      type: String,
      required: true
    },
  },
}
</script>

<style scoped>
.bin_card {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: space-evenly;
  flex-direction: row;
  font-weight: 500;
  font-size: 20px;
  line-height: 30px;
  background-color: #0F0F0F;
  border-radius: 10px;
  padding: 2% 0 2% 0;
}

.price {
  justify-content: space-between;
  text-align: left;
}
</style>
