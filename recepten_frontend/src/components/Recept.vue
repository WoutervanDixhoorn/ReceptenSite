<script>
export default {
    props: {
        title: String,
        ingredienten: [],
        content: String,
    },
}
</script>

<template>
    <div class="recept">
        <h1>{{ title }}</h1>
        <h2>Ingredienten</h2>
        <p v-for="ingredient in ingredienten" :key="ingredient.name">{{ ingredient.name + ' - ' + ingredient.amount + ' ' + ingredient.unit }}</p>
        <p style="white-space: pre; padding-top: 10px">{{ content }}</p>
    </div>
</template>

<style>
    .recept{
        padding-bottom: 0.5rem;
    }
    .recept h1{
        color: cadetblue;
    }
    .recept p{
        margin: 0;
    }
</style>