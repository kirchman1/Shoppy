<template>
    <div>
        <button class="btn" @click="toggleText()" >Edit</button>
        <form v-show="display">
            <input class="feo" v-model="image">
            <input v-model="title">
            <input v-model="desc">
            <input v-model="price">
            <button type="button" class="btn" @click="editData()">Save</button>
        </form>
    </div>
    

</template>

<script>
import axios from 'axios'

export default {
    props: ['item'],
    data() {
        return {
            display: false,
            image: this.item.image,
            title: this.item.title,
            desc: this.item.desc,
            price: this.item.price,
        }
    },
    methods: {
        toggleText() {
            this.display = !this.display
        },
        async editData() {
            try {
                const data = {
                    'image': this.image,
                    'title': this.title,
                    'desc': this.desc,
                    'price': this.price,
                }   
                
                const res = await axios.put(`http://127.0.0.1:8000/api/edit-item/${this.item.slug}`, data)
                if(res.data.result === 'Done')
                    this.display = false
            } catch(error) {
                console.error('Error:', error)
            };
        }
    }
}
</script>

<style scoped>

.btn {
    width: 100%;
    background-color: #3e8d78;
    height: 40px;
    margin-top: 10px;
    border: 1px solid silver;
    color: rgb(255, 255, 255);
    font-weight: bold;
    font-size: 14px;
    transition: transform 500ms ease;
    margin-bottom: 10px;
}

.btn:hover {
    cursor: pointer;
    transform: scale(1.03);
}

form input {
    width: 320px;
    padding: 10px 15px;
    border: 1.5px dashed #575d61;
    border-radius: 2px;
    background: #c8c9ca;
    display: block;
    color: #000000;
    outline: none;
    font-size: 15px;
    margin: 5px 0px;
    height: 12px;
}

form input:focus {
    border-color: #242424;
}

</style>