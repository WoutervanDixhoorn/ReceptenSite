<script>
export default {
    props: {
        title: String,
        content: String,
    },
}
</script>

<template>
    <div class="recept">
        <h1>{{ title }}</h1>
        <p>{{ content }}</p>
    </div>
</template>

<style>
    .recept{
        padding-bottom: 0.5rem;
    }
    .recept h1{
        color: cadetblue;
    }
</style>