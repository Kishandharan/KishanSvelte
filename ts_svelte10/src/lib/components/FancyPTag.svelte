<script lang="ts">
    interface propType1{
        text : string;
    }
    let props1 : propType1 = $props();
</script>

<p class="ptag">{props1["text"]}</p>

<style>
</style>