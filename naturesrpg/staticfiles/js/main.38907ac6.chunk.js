(this["webpackJsonpnature-rpg"] = this["webpackJsonpnature-rpg"] || []).push([
    [0], {
        104: function(e, t, c) {},
        115: function(e, t, c) {},
        118: function(e, t, c) {},
        229: function(e, t, c) {},
        238: function(e, t, c) {},
        239: function(e, t, c) {},
        242: function(e, t, c) {
            "use strict";
            c.r(t);
            var i = c(3),
                n = c.n(i),
                s = c(93),
                a = c.n(s),
                r = (c(104), c(20)),
                l = c(11),
                o = c(31),
                d = c(40),
                j = c.n(d),
                b = (c(115), c(1));
            var h = function(e) {
                    return Object(b.jsxs)("div", {
                        id: "profile-card",
                        children: [Object(b.jsx)("div", {
                            className: "profile-image",
                            children: Object(b.jsx)(j.a, {
                                image: e.image,
                                roundedColor: "rgba(36, 36, 36, .2)",
                                imageWidth: "85",
                                imageHeight: "85",
                                roundedSize: "8",
                                borderRadius: "70"
                            })
                        }), Object(b.jsx)("div", {
                            className: "profile-username",
                            children: e.username
                        }), Object(b.jsxs)("div", {
                            className: "profile-level",
                            children: ["Level ", e.level]
                        })]
                    })
                },
                m = c(16),
                O = c(95),
                u = c(42),
                x = (c(117), c(118), c.p+"staticfiles/media/prof.238d0e09.jpg"),
                v = function() {
                    var e = Object(i.useState)(!1),
                        t = Object(o.a)(e, 2),
                        c = t[0],
                        n = t[1],
                        s = function() {
                            n(!c)
                        };
                    return Object(b.jsx)(b.Fragment, {
                        children: Object(b.jsx)("div", {
                            id: "navbar",
                            children: Object(b.jsxs)(m.c, {
                                collapsed: !1,
                                children: [Object(b.jsx)(h, {
                                    image: x,
                                    username: "Ben_Johnson",
                                    level: "12"
                                }), Object(b.jsx)(m.d, {
                                    children: Object(b.jsxs)(m.a, {
                                        iconShape: "square",
                                        children: [Object(b.jsx)("div", {
                                            className: "home-menuItem",
                                            children: Object(b.jsxs)(m.b, {
                                                className: "home-menuItem",
                                                active: "/" === window.location.pathname,
                                                onClick: s,
                                                icon: Object(b.jsx)(u.b, {
                                                    className: "home-menuText"
                                                }),
                                                children: [Object(b.jsx)("div", {
                                                    className: "menu-text",
                                                    children: "Home"
                                                }), Object(b.jsx)(r.b, {
                                                    to: "/"
                                                })]
                                            })
                                        }), Object(b.jsx)("div", {
                                            className: "observation-menuItem",
                                            children: Object(b.jsxs)(m.b, {
                                                className: "observation-menuItem",
                                                active: "/observations" === window.location.pathname,
                                                onClick: s,
                                                icon: Object(b.jsx)(u.a, {
                                                    className: "observation-menuText"
                                                }),
                                                children: [Object(b.jsx)("div", {
                                                    className: "menu-text",
                                                    children: "Observations"
                                                }), Object(b.jsx)(r.b, {
                                                    to: "/observations"
                                                })]
                                            })
                                        }), Object(b.jsx)("div", {
                                            className: "battle-menuItem",
                                            children: Object(b.jsxs)(m.b, {
                                                className: "battle-menuItem",
                                                active: "/battle" === window.location.pathname,
                                                onClick: s,
                                                icon: Object(b.jsx)(O.a, {
                                                    className: "battle-menuText"
                                                }),
                                                children: [Object(b.jsx)("div", {
                                                    className: "menu-text",
                                                    children: "Battle"
                                                }), Object(b.jsx)(r.b, {
                                                    to: "/battle"
                                                })]
                                            })
                                        })]
                                    })
                                }), Object(b.jsx)(m.e, {
                                    children: Object(b.jsx)(m.a, {
                                        iconShape: "square",
                                        children: Object(b.jsxs)(m.b, {
                                            onClick: function() {
                                                alert("\n You think you can leave... how cute")
                                            },
                                            icon: Object(b.jsx)(u.c, {}),
                                            children: [" ", Object(b.jsx)("div", {
                                                className: "logout-text",
                                                children: "Logout"
                                            })]
                                        })
                                    })
                                })]
                            })
                        })
                    })
                },
                p = c(6),
                f = (c(229), c(43)),
                g = c.p + "staticfiles/media/header.85432ce2.svg";
            var k = function() {
                    return Object(b.jsx)("div", {
                        id: "dashboard",
                        children: Object(b.jsxs)(p.h, {
                            children: [Object(b.jsx)(p.j, {
                                children: Object(b.jsx)(p.g, {
                                    children: Object(b.jsxs)("div", {
                                        className: "dashboard-header",
                                        children: [Object(b.jsxs)("div", {
                                            className: "dashboard-header-text",
                                            children: [Object(b.jsx)("div", {
                                                className: "dashboard-header-text-header",
                                                children: Object(b.jsx)(f.Textfit, {
                                                    mode: "single",
                                                    children: "Welcome Back"
                                                })
                                            }), Object(b.jsxs)("div", {
                                                className: "dashboard-header-text-text",
                                                children: [Object(b.jsxs)(f.Textfit, {
                                                    mode: "single",
                                                    children: ["It looks like you have made ", Object(b.jsx)("strong", {
                                                        children: "2"
                                                    }), " new "]
                                                }), Object(b.jsx)(f.Textfit, {
                                                    mode: "single",
                                                    children: " observations while you were gone."
                                                })]
                                            })]
                                        }), Object(b.jsx)("img", {
                                            className: "dashboard-header-image",
                                            src: g,
                                            alt: "Adventurous person"
                                        })]
                                    })
                                })
                            }), Object(b.jsxs)(p.j, {
                                children: [Object(b.jsx)(p.g, {
                                    sm: "12",
                                    md: "6",
                                    lg: "6",
                                    children: Object(b.jsxs)(p.b, {
                                        className: "dashboard-card",
                                        children: [Object(b.jsx)(p.d, {
                                            children: "Card Title"
                                        }), Object(b.jsx)(p.c, {
                                            children: "Information"
                                        })]
                                    })
                                }), Object(b.jsx)(p.g, {
                                    sm: "12",
                                    md: "6",
                                    lg: "6",
                                    children: Object(b.jsxs)(p.b, {
                                        className: "dashboard-card",
                                        children: [Object(b.jsx)(p.d, {
                                            children: "Card Title"
                                        }), Object(b.jsx)(p.c, {
                                            children: "Information"
                                        })]
                                    })
                                }), Object(b.jsx)(p.g, {
                                    sm: "12",
                                    md: "6",
                                    lg: "6",
                                    children: Object(b.jsxs)(p.b, {
                                        className: "dashboard-card",
                                        children: [Object(b.jsx)(p.d, {
                                            children: "Card Title"
                                        }), Object(b.jsx)(p.c, {
                                            children: "Information"
                                        })]
                                    })
                                }), Object(b.jsx)(p.g, {
                                    sm: "12",
                                    md: "6",
                                    lg: "6",
                                    children: Object(b.jsxs)(p.b, {
                                        className: "dashboard-card",
                                        children: [Object(b.jsx)(p.d, {
                                            children: "Card Title"
                                        }), Object(b.jsx)(p.c, {
                                            children: "Information"
                                        })]
                                    })
                                })]
                            })]
                        })
                    })
                },
                N = (c(238), [{
                    title: "Observation Name",
                    image: "https://loremflickr.com/300/200/wildlife?random=1",
                    description: "Description",
                    key: 1
                }, {
                    title: "Observation Name",
                    image: "https://loremflickr.com/300/200/wildlife?random=2",
                    description: "Description",
                    key: 2
                }, {
                    title: "Observation Name",
                    image: "https://loremflickr.com/300/200/wildlife?random=3",
                    description: "Description",
                    key: 3
                }, {
                    title: "Observation Name",
                    image: "https://loremflickr.com/300/200/wildlife?random=4",
                    description: "Description",
                    key: 4
                }, {
                    title: "Observation Name",
                    image: "https://loremflickr.com/300/200/wildlife?random=5",
                    description: "Description",
                    key: 5
                }, {
                    title: "Observation Name",
                    image: "https://loremflickr.com/300/200/wildlife?random=6",
                    description: "Description",
                    key: 6
                }, {
                    title: "Observation Name",
                    image: "https://loremflickr.com/300/200/wildlife?random=7",
                    description: "Description",
                    key: 7
                }, {
                    title: "Observation Name",
                    image: "https://loremflickr.com/300/200/wildlife?random=8",
                    description: "Description",
                    key: 8
                }, {
                    title: "Observation Name",
                    image: "https://loremflickr.com/300/200/wildlife?random=9",
                    description: "Description",
                    key: 9
                }, {
                    title: "Observation Name",
                    image: "https://loremflickr.com/300/200/wildlife?random=10",
                    description: "Description",
                    key: 10
                }]),
                w = window.location.search,
                y = new URLSearchParams(w).get("username");

            function S(e) {
                return Object(b.jsx)(p.g, {
                    sm: "12",
                    md: "6",
                    lg: "4",
                    xl: "3",
                    children: Object(b.jsx)("div", {
                        className: "observation-card",
                        children: Object(b.jsxs)(p.b, {
                            children: [Object(b.jsx)(p.e, {
                                src: e.image,
                                top: "true"
                            }), Object(b.jsxs)(p.c, {
                                children: [Object(b.jsx)(p.f, {
                                    children: e.title
                                }), Object(b.jsx)("p", {
                                    children: e.body
                                })]
                            })]
                        })
                    })
                })
            }

            function C(e) {
                var t = e.search("square");
                return -1 !== t ? e.substring(0, t) + "large" + e.substring(t + 6) : e
            }
            var B = function() {
                    var e = Object(i.useState)(null),
                        t = Object(o.a)(e, 2),
                        c = t[0],
                        n = t[1],
                        s = Object(i.useState)(!1),
                        a = Object(o.a)(s, 2),
                        r = a[0],
                        l = a[1],
                        d = Object(i.useState)([]),
                        j = Object(o.a)(d, 2),
                        h = j[0],
                        m = j[1];
                    if (Object(i.useEffect)((function() {
                            fetch("https://api.inaturalist.org/v1/observations/?page=1&per_page=100&user_id=" + y).then((function(e) {
                                return e.json()
                            })).then((function(e) {
                                l(!0), m(e)
                            }), (function(e) {
                                l(!0), n(e)
                            }))
                        }), []), c) return Object(b.jsxs)("div", {
                        children: ["Error: ", c.message]
                    });
                    if (r) {
                        var O = Object(b.jsx)("div", {});
                        return null === y || 0 === h ? O = N.map((function(e) {
                            return Object(b.jsx)(S, {
                                title: e.title,
                                image: e.image,
                                body: e.description
                            }, e.key)
                        })) : (console.log(h.results), O = h.results.map((function(e) {
                            return Object(b.jsx)(S, {
                                title: e.taxon.name,
                                image: C(e.photos[0].url),
                                body: e.place_guess
                            }, e.key)
                        }))), Object(b.jsx)("div", {
                            id: "observations",
                            children: Object(b.jsxs)(p.h, {
                                className: "dr-example-container",
                                style: {
                                    paddingBottom: "20px"
                                },
                                children: [Object(b.jsx)(p.j, {
                                    children: Object(b.jsx)("h1", {
                                        className: "observations-header",
                                        children: "Observations"
                                    })
                                }), Object(b.jsx)(p.j, {
                                    children: O
                                })]
                            })
                        })
                    }
                    return Object(b.jsx)("div", {
                        children: "Loading..."
                    })
                },
                I = c(27),
                T = c(28),
                D = c(30),
                H = c(29),
                L = (c(239), function(e) {
                    Object(D.a)(c, e);
                    var t = Object(H.a)(c);

                    function c() {
                        return Object(I.a)(this, c), t.apply(this, arguments)
                    }
                    return Object(T.a)(c, [{
                        key: "render",
                        value: function() {
                            var e, t, c = (e = this.props.startHealth || this.props.health || 100, (t = this.props.health || 100) > .5 * e ? "success" : t > .2 * e ? "warning" : "danger");
                            return Object(b.jsx)(p.b, {
                                className: "battle-observation-card",
                                children: Object(b.jsxs)(p.c, {
                                    children: [Object(b.jsx)("div", {
                                        className: "observation-battle-image",
                                        children: Object(b.jsx)(j.a, {
                                            image: this.props.image || "https://loremflickr.com/300/200/cat?random=1",
                                            roundedColor: "rgba(36, 36, 36, .2)",
                                            imageWidth: "100",
                                            imageHeight: "100",
                                            roundedSize: "8",
                                            borderRadius: "70"
                                        })
                                    }), Object(b.jsx)("div", {
                                        children: this.props.name || "Observation Name"
                                    }), Object(b.jsxs)("div", {
                                        children: ["Level ", this.props.level || "1"]
                                    }), Object(b.jsxs)("div", {
                                        children: [this.props.health || "100", " hp / ", this.props.startHealth || this.props.health || "100", " hp"]
                                    }), Object(b.jsx)(p.i, {
                                        theme: c,
                                        value: this.props.health || "100",
                                        max: this.props.startHealth || this.props.health || "100"
                                    })]
                                })
                            })
                        }
                    }]), c
                }(i.Component));
            var M = function(e) {
                Object(D.a)(c, e);
                var t = Object(H.a)(c);

                function c(e) {
                    var i;
                    return Object(I.a)(this, c), (i = t.call(this, e)).state = {
                        action: -2,
                        inBattle: !1
                    }, i
                }
                return Object(T.a)(c, [{
                    key: "toggleBattle",
                    value: function() {
                        var e = this;
                        this.setState((function(t) {
                            return {
                                inBattle: !e.state.inBattle
                            }
                        }))
                    }
                }, {
                    key: "moveSelect",
                    value: function(e) {
                        this.setState((function(t) {
                            return {
                                action: e
                            }
                        }))
                    }
                }, {
                    key: "sumbitMove",
                    value: function(e) {
                        this.setState((function(e) {
                            return {
                                action: -2
                            }
                        })), -2 !== e ? console.log("Move submitted was " + e) : console.log("No move was selected")
                    }
                }, {
                    key: "render",
                    value: function() {
                        var e, t = this;
                        return this.state.inBattle ? Object(b.jsx)("div", {
                            id: "battle",
                            children: Object(b.jsxs)(p.h, {
                                children: [Object(b.jsxs)(p.j, {
                                    children: [Object(b.jsx)(p.g, {
                                        sm: "12",
                                        md: "6",
                                        children: Object(b.jsx)("div", {
                                            className: "observation-card",
                                            children: Object(b.jsx)(L, {
                                                startHealth: "150",
                                                health: "110",
                                                level: "12",
                                                name: "Jules the cat",
                                                image: "https://loremflickr.com/300/200/wildlife?random=1"
                                            })
                                        })
                                    }), Object(b.jsx)(p.g, {
                                        sm: "12",
                                        md: "6",
                                        children: Object(b.jsx)("div", {
                                            className: "observation-card",
                                            children: Object(b.jsx)(L, {})
                                        })
                                    })]
                                }), Object(b.jsxs)(p.j, {
                                    children: [Object(b.jsx)(p.g, {
                                        sm: "4",
                                        children: Object(b.jsx)("div", {
                                            className: "battle-button",
                                            children: Object(b.jsx)(p.a, {
                                                block: !0,
                                                theme: "danger",
                                                onClick: function() {
                                                    return t.toggleBattle()
                                                },
                                                children: "Leave"
                                            })
                                        })
                                    }), Object(b.jsx)(p.g, {
                                        sm: "4",
                                        children: Object(b.jsx)("div", {
                                            className: "battle-button",
                                            children: Object(b.jsx)(p.a, {
                                                block: !0,
                                                theme: "info",
                                                onClick: function() {
                                                    return t.moveSelect(1)
                                                },
                                                children: "Move 1"
                                            })
                                        })
                                    }), Object(b.jsx)(p.g, {
                                        sm: "4",
                                        children: Object(b.jsx)("div", {
                                            className: "battle-button",
                                            children: Object(b.jsx)(p.a, {
                                                block: !0,
                                                theme: "info",
                                                onClick: function() {
                                                    return t.moveSelect(2)
                                                },
                                                children: "Move 2"
                                            })
                                        })
                                    })]
                                }), Object(b.jsxs)(p.j, {
                                    children: [Object(b.jsx)(p.g, {
                                        sm: "4",
                                        children: Object(b.jsx)("div", {
                                            className: "battle-button",
                                            children: Object(b.jsx)(p.a, {
                                                block: !0,
                                                theme: "secondary",
                                                onClick: function() {
                                                    return t.moveSelect(0)
                                                },
                                                children: "Switch"
                                            })
                                        })
                                    }), Object(b.jsx)(p.g, {
                                        sm: "4",
                                        children: Object(b.jsx)("div", {
                                            className: "battle-button",
                                            children: Object(b.jsx)(p.a, {
                                                block: !0,
                                                theme: "info",
                                                onClick: function() {
                                                    return t.moveSelect(3)
                                                },
                                                children: "Move 3"
                                            })
                                        })
                                    }), Object(b.jsx)(p.g, {
                                        sm: "4",
                                        children: Object(b.jsx)("div", {
                                            className: "battle-button",
                                            children: Object(b.jsx)(p.a, {
                                                block: !0,
                                                theme: "info",
                                                onClick: function() {
                                                    return t.moveSelect(4)
                                                },
                                                children: "Move 4"
                                            })
                                        })
                                    })]
                                }), Object(b.jsx)(p.j, {
                                    children: Object(b.jsx)("div", {
                                        className: "battle-textbox",
                                        children: Object(b.jsx)(p.b, {
                                            children: Object(b.jsx)(p.c, {
                                                children: (e = this.state.action, -2 === e ? "Please select an option" : -1 === e ? "So... you would like to leave the match" : 0 === e ? "Switching to another observation I see..." : "You have chosen move " + e)
                                            })
                                        })
                                    })
                                }), Object(b.jsx)(p.j, {
                                    children: Object(b.jsx)(p.g, {
                                        sm: "3",
                                        children: Object(b.jsx)("div", {
                                            className: "battle-button",
                                            children: Object(b.jsx)(p.a, {
                                                block: !0,
                                                theme: "success",
                                                onClick: function() {
                                                    return t.sumbitMove(t.state.action)
                                                },
                                                children: "Submit"
                                            })
                                        })
                                    })
                                })]
                            })
                        }) : Object(b.jsxs)("div", {
                            className: "startBattleBox",
                            children: [Object(b.jsx)(p.a, {
                                className: "startBattleButton",
                                block: !0,
                                theme: "primary",
                                size: "lg",
                                onClick: function() {
                                    return t.toggleBattle()
                                },
                                children: "Battle vs AI"
                            }), Object(b.jsx)(p.a, {
                                block: !0,
                                disabled: !0,
                                theme: "secondary",
                                size: "lg",
                                onClick: function() {
                                    return t.toggleBattle()
                                },
                                children: "Battle vs Player"
                            })]
                        })
                    }
                }]), c
            }(n.a.Component);
            var z = function() {
                return Object(b.jsx)("div", {
                    className: "desktop-container",
                    children: Object(b.jsxs)(r.a, {
                        children: [Object(b.jsx)(v, {}), Object(b.jsxs)("div", {
                            className: "desktop-body",
                            children: [Object(b.jsx)("div", {
                                style: {
                                    color: "#ff0000",
                                    position: "absolute",
                                    right: "10px",
                                    top: "5px"
                                },
                                children: "The mobile version isn't complete"
                            }), Object(b.jsxs)(l.c, {
                                children: [Object(b.jsx)(l.a, {
                                    path: "/",
                                    exact: !0,
                                    component: k
                                }), Object(b.jsx)(l.a, {
                                    path: "/observations",
                                    component: B
                                }), Object(b.jsx)(l.a, {
                                    path: "/battle",
                                    component: M
                                })]
                            })]
                        })]
                    })
                })
            };
            var R = function() {
                    return Object(b.jsx)("div", {
                        className: "desktop-container",
                        children: Object(b.jsxs)(r.a, {
                            children: [Object(b.jsx)(v, {
                                collaspe: !0
                            }), Object(b.jsx)("div", {
                                className: "desktop-body",
                                children: Object(b.jsxs)(l.c, {
                                    children: [Object(b.jsx)(l.a, {
                                        path: "/",
                                        exact: !0,
                                        component: k
                                    }), Object(b.jsx)(l.a, {
                                        path: "/observations",
                                        component: B
                                    }), Object(b.jsx)(l.a, {
                                        path: "/battle",
                                        component: M
                                    })]
                                })
                            })]
                        })
                    })
                },
                E = 992,
                W = 768,
                J = 991,
                P = 767,
                _ = 320,
                q = 425,
                A = function() {
                    return {
                        width: window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
                        height: window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight
                    }
                },
                F = A(),
                U = F.width,
                Y = F.height,
                G = function(e) {
                    Object(D.a)(c, e);
                    var t = Object(H.a)(c);

                    function c() {
                        var e;
                        Object(I.a)(this, c);
                        for (var i = arguments.length, s = new Array(i), a = 0; a < i; a++) s[a] = arguments[a];
                        return (e = t.call.apply(t, [this].concat(s))).state = {
                            width: U,
                            height: Y
                        }, e.render = function() {
                            var t = e.props,
                                c = t.children,
                                i = t.displayIn,
                                s = e.state,
                                a = s.width,
                                r = s.height,
                                l = i.map((function(e) {
                                    return e.toLowerCase()
                                })),
                                o = e.shouldRender(l, a, r);
                            return Object(b.jsx)(n.a.Fragment, {
                                children: o ? c : null
                            })
                        }, e.handleResize = function() {
                            var t = A(),
                                c = t.width,
                                i = t.height;
                            e.setState({
                                width: c,
                                height: i
                            })
                        }, e.shouldRender = function(e, t, c) {
                            if (-1 !== e.indexOf("laptop") && t > c && t >= E) return !0;
                            if (-1 !== e.indexOf("tablet")) {
                                if (t <= J && t >= W) return !0;
                                if (1024 === t && 1366 === c) return !0
                            }
                            return -1 !== e.indexOf("mobile") && t <= P || (-1 !== e.indexOf("mobileportrait") && t <= P && c >= q || !!(-1 !== e.indexOf("mobilelandscape") && t <= P && c <= _))
                        }, e
                    }
                    return Object(T.a)(c, [{
                        key: "componentDidMount",
                        value: function() {
                            window.addEventListener("resize", this.handleResize, !1)
                        }
                    }, {
                        key: "componentWillUnmount",
                        value: function() {
                            window.removeEventListener("resize", this.handleResize, !1)
                        }
                    }]), c
                }(n.a.PureComponent);
            var K = function() {
                return Object(b.jsxs)(b.Fragment, {
                    children: [Object(b.jsx)(G, {
                        displayIn: ["Mobile"],
                        children: Object(b.jsx)(z, {})
                    }), Object(b.jsx)(G, {
                        displayIn: ["Tablet", "Laptop"],
                        children: Object(b.jsx)(R, {})
                    })]
                })
            };
            c(240), c(241);
            a.a.render(Object(b.jsx)(n.a.StrictMode, {
                children: Object(b.jsx)(K, {})
            }), document.getElementById("root"))
        }
    },
    [
        [242, 1, 2]
    ]
]);
//# sourceMappingURL=main.38907ac6.chunk.js.map