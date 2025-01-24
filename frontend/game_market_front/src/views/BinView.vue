
<script setup>
import Header from "@/components/Header.vue"
import Footer from "@/components/Footer.vue";
import BinCard from "@/components/BinCard.vue";

import {getAllFromBin, DeleteGameFromBin} from "@/api/WishList.js";
import {ref, onMounted} from "vue";
import {useAuthStore} from "@/stores/AuthStore.js";
import {useRouter} from "vue-router";


let games = ref([]);
let some_bool = true;

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
const price = () => {
  let pr = 0;
  games.value.forEach((game) => {
    pr += parseInt(game.game_information.price)
  })
  return pr
}
const delAll = async () => {
  for (let i =0 ;i<games.value.length;i++) {
    await DeleteGameFromBin(games.value[i].id)
  }
  some_bool = false;
  location.reload();
}

const logout = () => {
    authStore.logout()
    router.push('/login')
}

onMounted(async () => {
    await getAllGames();
    some_bool = games.value.length > 0
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
        <BinCard :game_name="game.game_information.game_name" :price="game.game_information.price" :ImagePath="game.game_information.game_img" :game_id="game.id"></BinCard>
      </div>
    </div>

    <div class="main_pay">
      <div class="to_pay">
        <div>Итого</div>
        <div>{{ price() }} Р</div>
      </div>
      <button
        class="auth_button" style="width: 100%"
        @click="delAll()"
      >Оплатить</button>
    </div>
  </div>

  <div v-else style="height: 40%;margin-top: 10%;margin-left: 5%">
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
