<script lang="ts">
  import {fade} from "svelte/transition";
  let showValue = $state(false);
</script>

<button onclick={ ()=> {showValue = !showValue} }>Toggle Visibility</button>
{#if showValue}
  <p transition:fade>I am visible</p>
{/if}
