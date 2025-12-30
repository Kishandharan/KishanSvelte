<script lang="ts">
    let inputElm : HTMLInputElement;
    let patients : string[] = [];
    let lPatients : number = 0;
    function handle1(){
        let value = inputElm.value;
        let uPatients = [];
        for(let i of patients){
            uPatients.push(i);
        }
        uPatients.push(value);
        patients = uPatients;
        lPatients = uPatients.length;
    }
</script>

<input placeholder="Enter patient name" bind:this={inputElm}>
<button on:click={handle1}>Add patient</button>
<p>Number of Patients: {lPatients}</p>


<ul>
    {#each patients as patient}
        <li>{patient}</li>
    {/each}
</ul>

<style>
</style>