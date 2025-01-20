<template>
<div class="card">
  <div class="image_rait">
    <div class="rating">{{rating}} rating</div>
    <img
        :src="currentImagePath"
        alt=""
        width="350px"
        height="400px"
        style="border-radius: 20px"
      />
  </div>
  <div class="game_name">{{gameName}}</div>
</div>
</template>

<script>
export default {
  name: "Card",
  props: {
    imagePath: {
      type: String,
      required: true,
    },
    rating: {
      type: String,
      required: true,
    },
    gameName: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      currentImagePath: "/src/assets/default.png", // По умолчанию путь к изображению-заглушке
    };
  },
  mounted() {
    this.checkImageExistence(this.imagePath);
  },
  methods: {
    checkImageExistence(imagePath) {
      const img = new Image();
      img.src = imagePath;

      img.onload = () => {
        this.currentImagePath = imagePath;
      };

      img.onerror = () => {
        console.warn(`Изображение по пути "${imagePath}" не найдено.`);
      };
    },
  },
};

</script>

<style scoped>
.image_rait {
font-size: 16px;
  font-weight: 600;
  line-height: 24px;
}
.rating {
  background-color: rgba(0, 0, 0, 5%);
  height: 32px;
  border-radius: 10px;
}
.game_name {
  font-size: 25px;
  font-weight: 500;
  line-height: 37px;
  text-align: center;
}
.card {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  width: 350px;
  margin: 5%;
}
</style>
