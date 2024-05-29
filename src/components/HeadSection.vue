<template>
    <div class="wrapper">
        <div>
            <h1>All items</h1>
            <h2>Best items for you</h2>
        </div>
        <div>
            <img src="/img/main-image.svg" alt="">
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style scoped>
.wrapper {
    background: #5CDDBC;
    width: 104%;
    position: relative;
    right: 13%;
    display: flex;
    padding: 0 12%;
    justify-content: space-between;
    align-items: center;
    height: 240px;
    color: #216F5B;
    margin: 60px 0;

}

.wrapper h1 {
    font-size: 70px;
    font-weight: bold;    
}

.wrapper h2 {
    font-size: 30px;
    font-weight: 400;
    margin-top: 15px;
    margin-bottom: 150px; 
}

.wrapper img {
    height: 230px;
    position: relative;
    top: 8px;
    right: 30px;
}
</style>