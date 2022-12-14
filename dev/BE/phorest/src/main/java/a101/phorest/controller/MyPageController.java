package a101.phorest.controller;

import a101.phorest.dto.PostDTO;
import a101.phorest.dto.UserDTO;
import a101.phorest.jwt.TokenProvider;
import a101.phorest.service.MyPageService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.Base64;
import java.util.List;

@Controller
@RequestMapping("api")
@RequiredArgsConstructor
public class MyPageController {
    private final MyPageService myPageService;

    private final TokenProvider tokenProvider;


    @ResponseBody
    @GetMapping("mypage/{username}")
    public UserDTO findByUserId(@PathVariable("username") String searchUsername, @RequestHeader(value = "Authorization", required = false) String token)
    {
        String loginUsername;
        if(searchUsername.equals("unkn0wnuser")) return null;
        if(token == null || token.equals("") || !tokenProvider.validateToken(token))
        {
            loginUsername = "";
        }
        else
        {
            loginUsername = (String)tokenProvider.getTokenBody(token).get("sub");
        }
        return myPageService.findByUserId(searchUsername, loginUsername);
    }

    @GetMapping("mypage/{username}/bookmark")
    @ResponseBody
    public List<PostDTO> findBookmarkedPost(@PathVariable("username") String username){
        return myPageService.findBookmarkPosts(username);
    }

    @PostMapping("mypage/{postId}/add")
    @ResponseBody
    public boolean addPost(@PathVariable("postId") String postIdEncoded, @RequestHeader("Authorization") String token){
        byte[] decodedBytes = Base64.getDecoder().decode(postIdEncoded);
        String decodedString = new String(decodedBytes);
        if(!decodedString.matches("[+-]?\\d*(\\.\\d+)?")) return false;
        Double decodedNumber = (Double.parseDouble(decodedString) - 37) / 73;
        Long postId = decodedNumber.longValue();
        if(postId - decodedNumber != 0)
            return false;
        if(!tokenProvider.validateToken(token))
            return false;

        String username = (String)tokenProvider.getTokenBody(token).get("sub");
        return myPageService.join(postId, username) != -1L;
    }


    @PostMapping("mypage/{postId}/share")
    @ResponseBody
    public Long sharePost(@PathVariable("postId") String postIdEncoded, @RequestHeader("Authorization") String token) {
        byte[] decodedBytes = Base64.getDecoder().decode(postIdEncoded);
        String decodedString = new String(decodedBytes);
        if(!decodedString.matches("[+-]?\\d*(\\.\\d+)?")) return 5L;
        Double decodedNumber = (Double.parseDouble(decodedString) - 37) / 73;
        Long postId = decodedNumber.longValue();
        if(postId - decodedNumber != 0)
            return 5L;
        if(!tokenProvider.validateToken(token))
            return 2L;
        String username = (String)tokenProvider.getTokenBody(token).get("sub");
        return myPageService.sharePost(postId, username);
    }
}
