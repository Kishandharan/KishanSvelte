<script lang="ts">
  import {page} from "$app/state";
  let lang = page.params.lang || "en";
</script>

{#if lang=="en"}
  <h1>Hello SvelteKit</h1>
{:else if lang=="sp"}
  <h1>Hola SvelteKit</h1>
{:else if lang=="fr"}
  <h1>Bonjour SvelteKit</h1>
{/if}
