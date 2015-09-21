var Browser = require("zombie");
var url = "http://localhost:3000";
var browser = new Browser();

var facebook_user = '**THA FACEBOOK USERNAME**';
var facebook_pass = '**THA FACEBOOK USERs PASSWORD**';

var registered_user = '**ALREADY REGISTERED USER**';
var registered_password = "**ALREADY REGISTERED USERs PASSWORD**";

/**/
                                                                                                                                                                            
describe("Login with email", function() {
   
    // Login form present --------------------------------------------------------
    it("should visit the site and see the login form", function(next) {
        browser.visit(url + '/login/login', function() {
            expect(browser.success).toBe(true);
            expect(browser.query("#LoginForm")).not.toBeNull();
            expect(browser.query("#login-username input[name=username]")).not.toBeNull();
            expect(browser.query("#login-password input[name=password]")).not.toBeNull();
            next();
        })
    });
    
    // Redirected to register when accessing profile new -------------------------
    it("should be redirected to login", function(next) {
        browser.visit(url + '/profile/new', function() {
            expect(browser.location.pathname).toBe("/login/register");
            next();
        })
    });    
    
    // Bad login -----------------------------------------------------------------
    it("should not be able to login with wrong credentials", function(next) {
        browser.visit(url + '/login/login', function() {
            browser
            .fill('#login-username input[name=username]', "wrongname")
            .fill('#login-password input[name=password]', "wrongpassword") 
                .pressButton('#login-submit button[type=submit]', function() {     
                    expect(browser.location.pathname).toBe("/login/login");
                    next();
            });
        });
    });
    
    // Good login -----------------------------------------------------------------
    it("should be able to login with the right credentials", function(next) {
        browser.visit(url + '/login/login', function() {
            browser
            .fill('#login-username input[name=username]', registered_user)
            .fill('#login-password input[name=password]', registered_password) 
            .pressButton('#login-submit button[type=submit]', function() {     
                    
                // Sign out link is shown for logged in users                  
                expect(browser.html("body")).toContain("Sign Out");
                    
                // No error message was received
                expect(browser.html("body")).not.toContain("Invalid E-Mail or Password");
                    
                next();
            });
        });
    });  
    
    // Logout ----------------------------------------------------------------
    it("should logout", function(next) {        
        browser.visit(url + '/profile/list/view', function() {   
            browser.clickLink("#t-logout a", function() {
                expect(browser.location.pathname).toBe("/login/index");
                next();
            });
        }); 
    });
    
});

/**/

describe("Login with facebook", function() {
    
    // Facebook login -----------------------------------------------------------------
    it("should login with facebook", function(next) {        
        browser.visit(url + '/fblogin', function() {   
            browser.wait(50000, function(){
                browser
                .fill('#email', facebook_user)
                .fill('#pass', facebook_pass) 
                .pressButton('#u_0_1', function() {
                    browser
                    .fill('#email', facebook_user)
                    .fill('#pass', facebook_pass) 
                    .pressButton('#u_0_1', function() {
                        expect(browser.html("body")).toContain("Sign Out");
                        next();         
                    });
                });
            });
        }); 
    });
    
    // Logout ----------------------------------------------------------------
    it("should logout", function(next) {        
        browser.visit(url + '/profile/list/view', function() {   
            browser.clickLink("#t-logout a", function() {
                console.log(browser.location.pathname);
                expect(browser.location.pathname).toBe("/login/index");
                next();
            });
        }); 
    });
});

/**/

