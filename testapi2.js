$(function() {
    // 첫 번째 버튼 클릭 시 이벤트 핸들러
    $("#cat1").click(function() {
        // 서버로 고양이 정보 요청 (API 경로: /spring/api/catOne)
        $.get("/spring/api/catOne", function(data) {
            // JSON 데이터를 문자열로 변환하고 다시 JSON 객체로 파싱
            var x = JSON.stringify(data);
            var jo = JSON.parse(x);
            
            // 팝업 창에 고양이 정보 출력
            var popupText = "이름: " + jo.name + " 나이: " + jo.age;
            window.alert(popupText); // 팝업 창 열기
        });
    });

    // 두 번째 버튼 클릭 시 이벤트 핸들러
    $("#cat2").click(function() {
        // 새 XMLHttpRequest 객체 생성
        var xhr = new XMLHttpRequest();
        
        // 서버로 고양이 정보 요청 (API 경로: /spring/api/catTwo)
        xhr.open('GET', '/spring/api/catTwo');
        xhr.send();
        
        // 요청이 완료되었을 때 실행되는 이벤트 핸들러
        xhr.onload = function() {
            if (xhr.status === 200) { // 성공적인 응답 확인
                // 서버에서 받은 JSON 문자열을 객체로 파싱
                var j = xhr.responseText;
                var jo = JSON.parse(j);
                
                // 팝업 창에 고양이 정보 출력
                var popupText = "이름: " + jo.name + " 나이: " + jo.age;
                window.alert(popupText); // 팝업 창 열기
            } else { // 요청 실패
                console.error(xhr.statusText);
            }
        };
    });
});
