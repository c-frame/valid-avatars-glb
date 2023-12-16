# The Validated Avatar Library for Inclusion and Diversity (VALID)

This is all the [VALID avatars](https://github.com/xrtlab/Validated-Avatar-Library-for-Inclusion-and-Diversity---VALID) converted to glTF.

210 avatars listed in [avatars.json](avatars.json).

You can use this repo directly from the CDN jsdelivr to create a UI to select an avatar for example.

Example of code to download the list of avatars, create the image url and model url to download them:

```js
const avatarsBaseUrl = 'https://cdn.jsdelivr.net/gh/c-frame/valid-avatars-glb@c539a28/';
const fetchAvatars = async () => {
  const response = await fetch(avatarsBaseUrl + 'avatars.json');
  if (!response.ok) {
    return [];
  }
  const results = await response.json();
  console.log(results);
  results.forEach((entry) => {
    console.log(avatarsBaseUrl + entry.image);
    console.log(avatarsBaseUrl + entry.model);
  });
  return results;
};
fetchAvatars()
```

For a demo of using those avatars with networked-aframe, [see this repo](https://github.com/networked-aframe/naf-valid-avatars).
