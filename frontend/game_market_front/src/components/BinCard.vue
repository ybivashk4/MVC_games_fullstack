<template>
  <div class="bin_card">
    <img :src="ImagePath" alt="" height="122px" width="220px">
    <div>{{game_name}}</div>
    <div class="flex-column price">
      <div>
        {{price}} Р
      </div>
      <button style="margin-left: 100%;width: 200%;height: 40%" class="change_text_color" @click="this.delete()">
        Удалить
      </button>
    </div>
  </div>
</template>

<script>
import {DeleteGameFromBin} from "@/api/WishList.js";

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
    game_id: {
      type: String,
      required: true
    }
  },
  methods: {
    async delete() {
      await DeleteGameFromBin(this.game_id);
      location.reload();

    }
  }
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
