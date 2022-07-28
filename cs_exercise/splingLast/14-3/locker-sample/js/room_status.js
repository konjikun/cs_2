let BASE_URL = "https://edu-iot.iniad.org/api/v1";

function displayRoomStatus(result) {
humidity.textContent
}

function getRoomStatus() {
  // let userid =
  let userid =document.getElementById("iniad-id")
  let userId = userid.value

  // let userpw =
  let userpw = document.getElementById("iniad-pw")
let userPw =userpw.value

  // let roomNum =
  let roomNum = document.getElementById("room-number")
  roomNumber = roomNum.value

  // let url =
  let url = BASE_URL + "sencors" + roomNumber

  callRoomStatusAPI(url, 'GET', userId, userPw, displayRoomStatus);
}

