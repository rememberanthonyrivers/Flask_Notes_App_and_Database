function deleteNote(noteId){ // takes in the note id we created 

    fetch('/delete-note', { // then we send a post request to the delete note endpoint

        method: "POST",

        body: JSON.stringify({ noteId: noteId }),

    }).then((_res) => {
        
        window.location.href = "/"; // now we will refresh the page with the home page 
        
    });
}