$( document ).ready(function() {

});

//console.log('Heelowwww')
//
//
//const url = window.location.href
//
//const searchForm = document.getElementById("search-form")
//const searchInput = document.getElementById("search-input")
//const resultsBox = document.getElementById("search-results")
//
//
//const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
//
//
//options = {method: "GET",
//		   headers: {
//		   	Accept: "application/json"
//		   },
//		   data:{
//		   	'csrfmiddlewaretoken': csrf,
//		   	'search_input': searchInput
//		   }
//}
//
//
//
//
//
//const SearchPosts = async SearchIt => {
//const res = await fetch("http://127.0.0.1:8000/user/search",options)
//const Posts = await res.json()
//
//console.log(Posts)
//const regex = new RegExp(`^${SearchIt}`, 'r')
//
//for (var i = 0; i < Posts.data.length; ++i) {
//	if (Posts.data[i].username.match(regex)){
//		resultsBox.innerHTML = `<b>${Posts.data[i].username}</b>
//		<img class="rounded-circle account-img"src = "${Posts.data[i].user_profile__profile_picture}">`
//		console.log(Posts.data[i].username)
//	}
//
//}
//}
//
//
//
//
//searchInput.addEventListener('input', () => {
//	SearchPosts(searchInput.value)
//	if (resultsBox.classList.contains("not-visible")) {
//		resultsBox.classList.remove("not-visible")
//	}
//})