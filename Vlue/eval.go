package main

import (
	"fmt"
	"io"

	"github.com/alecthomas/participle/v2"
	"github.com/alecthomas/repr"
	"golang.org/x/tools/go/analysis/passes/nilfunc"
)

type Evaluatable interface {
	Eval(ctx *Context) (interface{}, error)
}

type Function func(args ...interface{}) (interface{}, error)

type Context struct {
	Functions map[string]Function
	Vars      map[string]interface{}
	Input     io.Reader
	Output    io.Writer
}

func (p *Program) init() {
	p.Table = map[int]*Statement{}
	for index, stmt := range p.Statements {
		stmt.Index = index
		p.Table[stmt.Pos.Offset] = stmt
	}
}

func (v *Value) Eval(ctx *Context) (interface{}, error) {
	switch {
	case v.Number != nil:
		return *v.Number, nil
	case v.Bool != nil:
		return *v.Bool, nil
	case v.String != nil:
		return *v.String, nil
	case v.Undefined != nil:
		return false, nil
	case v.SubExpression != nil:
		return
	}
	panic("unsupported value type " + repr.String(v))
}

func (u *Unary) Eval(ctx *Context) (interface{}, error) {
	if u.Value != nil {
		return *u.Value, nil
	}

	if u.Unary != nil {
		switch {
		case *u.Op == "!":
			j, err := u.Unary.Eval(ctx)
			if err != nil {
				panic(err)
			}
			switch j.(type) {
			case float64:
				if j == 0 {
					return false, nil
				} else {
					return true, nil
				}
			case string:
				if j == "0" || j == "false" {
					return false, nil
				} else {
					return true, nil
				}
			case bool:
				return !j.(bool), nil
			}
		case *u.Op == "-":
			j, err := u.Unary.Eval(ctx)
			if err != nil {
				panic(err)
			}
			switch j.(type) {
			case float64:
				return -j.(float64), nil
			default:
				return nil, fmt.Errorf("uminus requires float64.")
			}
		}
	}

	panic("unreachable")
}

func (m *Multiplication) Eval(ctx *Context) (interface{}, error) {
	lhs, err := m.Unary.Eval(ctx)
	if err != nil {
		return nil, err
	}
	op := m.Op
	rhs, err := m.Next.Eval(ctx)
	if err != nil {
		return nil, err
	}
	switch *op {
	case "*":
		if lhs.(type) == rhs.(type) {

		}
	}
}
