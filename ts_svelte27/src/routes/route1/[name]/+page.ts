import type {PageLoad} from "./$types";

export const load: PageLoad = async ({params}) => {
  return {
    "data":"Your name is "+params.name
  };
};
