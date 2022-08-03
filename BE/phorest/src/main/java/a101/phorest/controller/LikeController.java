package a101.phorest.controller;

import a101.phorest.dto.PostDto;
import a101.phorest.jwt.TokenProvider;
import a101.phorest.service.LikeService;
import a101.phorest.service.MyPageService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@Controller
@RequestMapping("api")
@RequiredArgsConstructor
public class LikeController {
    private final LikeService likeService;

    public final TokenProvider tokenProvider;

    @GetMapping("community/{postId}/like")
    @ResponseBody
    public boolean addPost(@PathVariable("postId") Long postId, @RequestHeader("Authorization") String token){
        if(!tokenProvider.validateToken(token))
            return false;
        String username = (String)tokenProvider.getTokenBody(token).get("sub");
        likeService.join(postId, username);
        return true;
    }
}
