<script setup>
import Header from "@/components/Header.vue"
import Footer from "@/components/Footer.vue";
import {onMounted} from "vue";
import {getAllFromWishlist, getAllFromBin} from "@/api/WishList.js";
import {ref} from "vue";
</script>

<template>
  <Header></Header>

<div class="main_description">
    <h3>{{game.game_name}}</h3>
    <div class="description">
      <div class="card">
        <img
          :src="game.game_img"
          alt=""
          width="350px"
          height="400px"
          style="border-radius: 20px"
        />
        <div class="under_img" >
          <div>{{ game.price }} Р</div>

          <button v-if="is_in_bin" class="auth_button bin_after_button" @click="change_bin()">
            В корзине
          </button>

          <button v-else class="auth_button" @click="change_bin()">
            В корзину
          </button>

        </div>
          <button
            v-if="is_in_wishlist" class="wishlist_button wishlist_button_after" style="margin-top: 5%;width: 100%" @click="change_wishlist()">
            <img src="/src/assets/wishlisst_after.svg" alt=""> В списке желаемого
          </button>

          <button
            v-else class="wishlist_button" style="margin-top: 5%;width: 100%" @click="change_wishlist()">
            <img src="/src/assets/wishlisst.svg" alt=""> В список желаемого
          </button>

      </div>
      <div class="flex-column" style="margin-top: 5%">
        <div class="change_text_color up_text_description">
          <div>{{game.rating}} rating</div>
          <div>{{ game.is_multiplayer ? 'Мультиплеер' : 'Одиночная' }}</div>
        </div>
        <div style="display: flex;margin-top: 4vh">
          <div style="text-align: left">

            <div class="change_text_color">
              Жанр
            </div>
            <div class="change_text_color">
              Язык
            </div>
            <div class="change_text_color">
              Дата выхода
            </div>
            <div class="change_text_color">
              Разработчик
            </div>
            <div class="change_text_color">
              Особенности
            </div>

          </div>

          <div style="text-align: left;margin-left: 5vh">

            <div>
              {{ game.genre }}
            </div>
            <div>
              {{game.language}}
            </div>
            <div>
              {{ game.date }}
            </div>
            <div>
              {{ game.developer }}
            </div>
            <div>
              {{ game.specialties }}
            </div>

          </div>

        </div>
        <div class="big_description">
          {{
            game.description
          }}
        </div>
      </div>

    </div>


  </div>

  <Footer></Footer>


</template>

<style scoped>
.card {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  width: 350px;
  margin: 5%;
}

.under_img {
  display: flex;
  justify-content: space-evenly;

  text-align: center;
  font-size: 24px;
  font-weight: 700;
  line-height: 36px;
  margin-top: 5%;
}

.main_description {
  display: flex;
  width: 80%;
  flex-direction: column;
}

.description {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: space-around;
  font-size: 18px;
  line-height: 27px;
  font-weight: 500;
}

.up_text_description {
  display: flex;
  justify-content: space-between;
  width: 28vh;
}


.big_description {
  text-align: left;
  width: 70%;
  margin-top: 5%;
}
.wishlist_button {
  width: 100%;
  background-color: #141414;
  border-color: #999999;
  border-radius: 5px;
  height: 3vh;
  color: #999;

}
.bin_after_button {
  background-color: #141414;
  color: #009AB6;
  border-color: #009AB6;
}
.wishlist_button_after {
  color: white;
}
</style>

<script>
import {getGame} from "@/api/catalog.js";
import {
  AddToWishList,
  AddToBin,
  DeleteGameFromWishlist,
  DeleteGameFromBin,
  GetFromToBin,
  GetFromWishList,
  getAllFromWishlist, getAllFromBin
} from "@/api/WishList.js"
import {ref} from "vue";
export default {
  data() {
    return {
      game: {},
      is_in_wishlist: false,
      is_in_bin: false
    };
  },
  async created() {
    const game_id = this.$route.params.id;
    this.get_game_info();
    this.get_info_wishlist();
    this.get_info_bin();
  },
  methods: {
    async get_game_info() {
      const game_id = this.$route.params.id;
      try {
        const response = await getGame(game_id);
        this.game = response;
      } catch (e) {
        console.error(e);
      }
    },
    async get_info_wishlist() {
      let gamesFromWishlist = ref([]);

      gamesFromWishlist.value = await getAllFromWishlist();
      gamesFromWishlist.value.forEach((game) => {
        if (!this.is_in_wishlist) this.is_in_wishlist = parseInt(game.game_information.id) === parseInt(this.$route.params.id)
        console.info(game.game_information.id, this.$route.params.id)
      })
    },
    async get_info_bin() {
      let gamesFromBin = ref([])
      gamesFromBin.value = await getAllFromBin();
      const game_id = this.$route.params.id;
      gamesFromBin.value.forEach((game) => {
        if (!this.is_in_bin)  this.is_in_bin = game.game_information.id === parseInt(this.$route.params.id)
      })
    },
    async change_wishlist() {
      let gamesFromWishlist = ref([]);
      gamesFromWishlist.value = await getAllFromWishlist();
      let game_id = -1;

      if (this.is_in_wishlist) {
        gamesFromWishlist.value.forEach(
          (game) => {
            if (game_id == -1)
            game_id = parseInt(this.$route.params.id) === parseInt(game.game_information.id) ? parseInt(game.id) : -1;
          }
        )
        if (game_id != -1)  await DeleteGameFromWishlist(game_id)
        this.is_in_wishlist = false
      } else {
        await AddToWishList(this.$route.params.id)
        this.is_in_wishlist = true
      }
    },
    async change_bin() {
      let gamesFromBin = ref([]);
      gamesFromBin.value = await getAllFromBin();
      let game_id = -1;
      if (this.is_in_bin) {
        gamesFromBin.value.forEach(
          (game) => {
            if (game_id == -1)
            game_id = parseInt(this.$route.params.id) === parseInt(game.game_information.id) ? parseInt(game.id) : -1;

            console.info(game.id)
          }
        )
        if (game_id != -1)  await DeleteGameFromBin(game_id)
        this.is_in_bin = false
      } else {
        await AddToBin(game_id)
        this.is_in_bin = true
      }
    },
  },
}
</script>
