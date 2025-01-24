
<script setup>

import Card from "@/components/Card.vue";
import Header from "@/components/Header.vue"
import Footer from "@/components/Footer.vue";
import {getAllFromWishlist} from "@/api/wishlist.js";
import {ref, onMounted} from "vue";
import {useAuthStore} from "@/stores/AuthStore.js";
import {LogOut} from "lucide-vue-next";
import {useRouter} from "vue-router";


let games = ref([]);

const router = useRouter()
const authStore = useAuthStore();
const getAllGames = async () => {
  try {
    games.value = await getAllFromWishlist();
  }
  catch (e) {
    console.log(e);
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
  <div class="catalog">
    <h3>Список желаемого</h3>
    <div class="all_games">
      <div v-for="(game, index) in games" :key="index">
        <Card :game-name="game.game_information.game_name" :rating="game.game_information.rating" :image-path="game.game_information.game_img" :game-id="game.game_information.id"></Card>
      </div>
    </div>

  </div>

  <Footer></Footer>
</template>



<style scoped>
.catalog {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  width: 100%;
}

.all_games {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  margin-left: 10%;
  margin-right: 10%;
  width: 70%;
}
</style>
