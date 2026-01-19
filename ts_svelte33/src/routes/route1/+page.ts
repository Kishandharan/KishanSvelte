import type {PageLoad} from "./$types";

export const load:PageLoad = async() => {
  await new Promise(r=>setTimeout(r, 5000));
  console.log("+page.ts loaded successfully.");
  return {};
};
