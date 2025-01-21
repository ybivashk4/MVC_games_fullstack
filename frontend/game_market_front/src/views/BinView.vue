
<script setup>
import Header from "@/components/Header.vue"
import Footer from "@/components/Footer.vue";
import BinCard from "@/components/BinCard.vue";
const some_bool = true;

import {getAllFromBin, DeleteGameFromBin} from "@/api/WishList.js";
import {ref, onMounted} from "vue";
import {useAuthStore} from "@/stores/AuthStore.js";
import {useRouter} from "vue-router";


let games = ref([]);

const router = useRouter()
const authStore = useAuthStore();
const getAllGames = async () => {
  try {
    games.value = await getAllFromBin();
  }
  catch (e) {
    console.warn(e);
  }
}
const logout = () => {
    authStore.logout()
    router.push('/login')
}
onMounted(async () => {
    await getAllGames();
    if (authStore.authError) {
        logout()
    }
})
</script>


<template>
  <Header></Header>
  <h3>Корзина</h3>
  <div class="main_bin" v-if="some_bool">
    <div class="in_bin">
      <div v-for="(game, index) in games" :key="index">
        <BinCard :game_name="game.game_name" :price="game.rating" :image-path="game.game_img"></BinCard>
      </div>
    </div>

    <div class="main_pay">
      <div class="to_pay">
        <div>Итого</div>
        <div>4948 Р</div>
      </div>
      <button class="auth_button" style="width: 100%">Оплатить</button>
    </div>
  </div>

  <div style="height: 40%;margin-top: 10%;margin-left: 5%" v-else>
    <div>
      <img src="/src/assets/empty_bin.svg" alt="">
    </div>
    <div>
      Ваша корзина пуста
    </div>
  </div>

  <Footer></Footer>
</template>

<script>
export default {
  name: "BinView"
}
</script>

<style scoped>
.main_bin {
  width: 80%;
  height: 80%;
  display: flex;
  flex-direction: row;
  margin-left: 10%;
  margin-top: 5%;
}

.in_bin {
  width: 60%;
  height: 90%;
  display: flex;
  flex-direction: column;
  margin-right: 5%;
}

.main_pay {
  display: flex;
  width: 20%;
  flex-direction: column;
  align-items: center;
  font-size: 27px;
  font-weight: 700;
  line-height: 43px;
}
.to_pay {
  display: flex;
  width: 100%;
  justify-content: space-between;
  margin-bottom: 5%;
}

</style>
