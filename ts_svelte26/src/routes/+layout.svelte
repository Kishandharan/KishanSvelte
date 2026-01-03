<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
  import "$lib/app.css";
	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="topbar">
  <a href="/createbooks" class="tbhl">Create Books</a>
  <a href="/viewbooks" class="tbhl">View Books</a>
  <a href="/deletebooks" class="tbhl">Delete Books</a>
</div>

{@render children()}

