package a101.phorest.controller;

import a101.phorest.dto.UserDTO;
import a101.phorest.jwt.TokenProvider;
import a101.phorest.service.MyPageService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

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
        if(token == null)
        {
            loginUsername = "";
        }
        else if(tokenProvider.validateToken(token))
        {
            loginUsername = (String)tokenProvider.getTokenBody(token).get("sub");
        }
        else
        {
            return new UserDTO();
        }
        return myPageService.findByUserId(searchUsername, loginUsername);
    }

    @PostMapping("mypage/{postId}/add")
    @ResponseBody
    public boolean addPost(@PathVariable("postId") Long postId, @RequestHeader("Authorization") String token){
        if(!tokenProvider.validateToken(token))
            return false;
        String username = (String)tokenProvider.getTokenBody(token).get("sub");
        return myPageService.join(postId, username) != -1L;
    }


    @PostMapping("mypage/{postId}/share")
    @ResponseBody
    public Long sharePost(@PathVariable("postId") Long postId, @RequestHeader("Authorization") String token)
    {
        if(!tokenProvider.validateToken(token))
            return 1L;

        String username = (String)tokenProvider.getTokenBody(token).get("sub");
        return myPageService.sharePost(postId, username);
    }
}
