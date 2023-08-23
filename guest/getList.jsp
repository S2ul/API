<%@page import="com.peisia.domain.GuestVO"%>
<%@page import="java.util.List"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>방명록 - 글 목록</title>
<link rel="stylesheet" href="/resources/common.css" >
</head>
<body>
<h1>방명록</h1>
<h2>글목록</h2>
<table>
	<tr>
		<td>번호</td>
		<td>내용</td>
	</tr>
	
<%
	Object o = request.getAttribute("list");
	List<GuestVO> list = (List<GuestVO>)o; 
	for(int i=0;i<list.size();i++){
		Long bno = list.get(i).getBno();
		String btext = list.get(i).getBtext();
%>	
	<tr>
		<td><%=bno %></td>
		<td><a href="/spring/guest/read?bno=<%=bno%>"> <%=btext %> </a></td>
	<tr>
<%		
	}
%>
</table>

<br><br>

<!-- [ ] 글쓰기 페이지로 이동 -->
<a href="/spring/guest/write">새글 쓰기</a>

</body>
</html>