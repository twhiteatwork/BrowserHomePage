//Javascript file referenced by base.html template

//Function called from home.html template to delete link on button click
function deleteLink(LinkID) {
    fetch("/delete", {
      method: "POST",
      body: JSON.stringify({ LinkID: LinkID }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }